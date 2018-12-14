import unittest
import json
from falcon import testing, falcon

import app
import tests.test_orders_data as testdata
import orders.spec as spec

class TestBase(testing.TestCase):
    def setUp(self):
        super(TestBase, self).setUp()
        self.app = app.create()

class TestOrders(TestBase):

    order_endpoint = '/orders'

    def assertOrderExists(self, order_sent, server_orders):
        order_list = []
        for order in server_orders:
            server_order_init_format = {
                spec.order_symbol_key: order[spec.order_symbol_key],
                spec.order_quantity_key: order[spec.order_quantity_key],
                spec.order_type_key: order[spec.order_type_key],
            }
            order_list.append(server_order_init_format)
        if order_sent not in order_list:
            raise AssertionError("Order " + str(order_sent) + " is not found on server")

    def test_get_message(self):
        result = self.simulate_get('/orders')
        # for individual_resp in resp:
            # assert "orders" in individual_resp


    def test_post_order(self):
        self.post_order_test_handler(\
            testdata.std_post_data,\
            testdata.std_post)
        self.post_order_test_handler(\
            testdata.wrong_json_format_post_data,\
            testdata.wrong_json_format_post)

    def test_get_order(self):
        self.get_order_test_handler(\
            testdata.std_post_data,\
            testdata.std_post_data[spec.data_key][spec.trader_id_key])
        pass

    def test_order_matching(self):
        pass

    def get_order_test_handler(self, payload, trader_id=None):
        if (type(payload) == list):
            for p in payload:
                self.simulate_post('/orders', json=p)
        else:
            self.simulate_post('/orders', json=payload)
        if trader_id == None:
            self.handle_get_all_orders()
        else:
            self.handle_get_trader_order(trader_id, payload[spec.data_key][spec.order_key])

    def handle_get_trader_order(self, trader_id, data_sent):
        param = {"trader_id": trader_id}
        result = self.simulate_get(self.order_endpoint, params=param)
        resp = result.json
        self.assertIn(spec.data_key, resp)
        for order in data_sent:
            self.assertOrderExists(order, resp[spec.data_key])

    def handle_get_all_trade_order(self, data_sent):
        result = self.simulate_get(self.order_endpoint)
        resp = result.json
        if spec.data_key not in resp:
            '''Expect getting order data from multiple traders'''
        else:
            '''Expect getting data from one trading account'''
            for order_item in data_sent:
                self.assertOrderExists(order_item, resp[spec.data_key])

    def post_order_test_handler(self, payload, test_type):
        result = self.simulate_post('/orders', json=payload)
        resp = result.json
        if test_type == testdata.std_post:
            assert spec.resp_msg_key in resp
            assert spec.post_success_resp_msg in resp["Message"]
            assert falcon.HTTP_201 == result.status
        elif test_type == testdata.wrong_json_format_post:
            assert spec.resp_msg_key in resp
            assert spec.post_json_missing_key_err_msg in resp["Message"]
            assert falcon.HTTP_400 == result.status
        elif test_type == testdata.non_numerical_quantity_post:
            pass

# if __name__ == "__main__":
#     unittest.main()
