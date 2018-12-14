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

    def get_order_test_handler(self, payload, trader_id):
        self.simulate_post('/orders', json=payload)
        print(payload)
        if trader_id == None:
            self.handle_get_all_orders()
        else:
            self.handle_get_trader_order(trader_id, payload[spec.data_key][spec.order_key])

    def handle_get_trader_order(self, trader_id, db_data):
        param = {"trader_id": trader_id}
        result = self.simulate_get(self.order_endpoint, params=param)
        resp = result.json
        self.assertIn(spec.data_key, resp)
        for order in resp[spec.data_key]:
            self.assertIn(spec.order_symbol_key, order)
            self.assertIn(spec.order_quantity_key, order)
            self.assertIn(spec.order_type_key, order)
            pass
            # order_on_init = {
            #     spec.order_symbol_key: order[spec.order_symbol_key],
            #     spec.order_quantity_key: order[spec.order_quantity_key],
            #     spec.order_type_key: order[spec.order_type_key],
            # }
            # self.assertEqual(order, order_on_init)

    def handle_get_all_trade_order(self):
        result = self.simulate_get(self.order_endpoint)


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
