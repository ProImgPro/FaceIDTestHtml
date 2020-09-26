from odoo import api, fields, models
import requests
import json
import os
from os import listdir


class ProviderAhamove(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(selection_add=[('aha_move', 'AhaMove')])
    token_aha = fields.Char(string="Token AhaMove")


    def aha_move_rate_shipment(self, order):
        carrier = self._match_address(order.partner_shipping_id)

        # Get address of warehouse
        search_token_aha = self.env['sale.order'].search([], limit=1)
        address_warehouse = []
        for name in search_token_aha:
            address_warehouse.append(name.warehouse_id.partner_id.street)

        # Get Token Of Delivery Order
        search_token_aha = self.env['choose.delivery.carrier'].search([])
        list_token_aha = []
        for i in search_token_aha:
            list_token_aha.append(i.carrier_id.token_aha)

        # Get Address of User. That's address of Company
        header = 'https://apistg.ahamove.com/v1/order/create?token='
        rail = '&service_id=SGN-BIKE&&requests=[]'
        token = list_token_aha[-1]
        add_sender =  '{"address"' + ":" + '"' + address_warehouse[0] + '"' + '}'
        add_receiver = '{"address"'+ ":" + '"' + order.partner_shipping_id.street + '"' + '}'

        # Post Url to get rate
        url = header + token + f'&order_time=0&path=[{add_sender},{add_receiver}]' + rail
        res = requests.post(url)
        load_json_response = json.loads(res.text)
        print('json.loads(res.text)', json.loads(res.text))
        price = float(load_json_response['order']['total_pay'])

        # Delete Text In File
        link_text = 'local_addons/delivery_ahamove/static/share_link/container.txt'
        open(link_text, 'w').close()

        # Save Share Link
        shark_link = str(load_json_response['shared_link'])
        text_file = open(link_text, "w")
        n = text_file.write(shark_link)
        text_file.close()

        return {'success': True,
                'price': price,
                'error_message': False,
                'warning_message': False}


    def aha_move_send_shipping(self, pickings):
        res = []
        for p in pickings:
            res = res + [{'exact_price': p.carrier_id.fixed_price,
                          'tracking_number': True}]

        return res

    def aha_move_get_tracking_link(self, picking):
        my_file_handle = open("local_addons/delivery_ahamove/static/share_link/container.txt")
        read_file_link = my_file_handle.read()
        return read_file_link



