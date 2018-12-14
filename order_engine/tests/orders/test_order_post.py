import falcon

from tests.orders.test_order_classes import TestOrders
import tests.orders.test_orders_data as testdata
import orders.spec as spec

class TestOrdersPost(TestOrders):

    def test_post_order(self):
        self.post_order_test_handler(\
            testdata.std_post_data,\
            testdata.std_post)
        self.post_order_test_handler(\
            testdata.wrong_json_format_post_data,\
            testdata.wrong_json_format_post)

    def post_order_test_handler(self, payload, test_type):
        result = self.simulate_post('/orders', json=payload)
        resp = result.json

        if test_type == testdata.std_post:
            self.assertIn(spec.resp_msg_key, resp)
            self.assertIn(spec.post_success_resp_msg, resp["Message"])
            self.assertEqual(falcon.HTTP_201, result.status)

            trader_id = payload[spec.data_key][spec.trader_id_key]
            orders_to_post = payload[spec.data_key][spec.order_key]

            # verify data is posted in database
            param = {"trader_id": trader_id}
            verify_data = self.simulate_get(self.order_endpoint, params=param)
            resp = verify_data.json
            for order in resp[spec.data_key]:
                self.assertIn(spec.order_symbol_key, order)
                self.assertIn(spec.order_quantity_key, order)
                self.assertIn(spec.order_type_key, order)
                self.assertIn(spec.order_status_key, order)
                self.assertIn(spec.order_time_key, order)
            for order in orders_to_post:
                self.assertOrderExists(order, resp[spec.data_key])

        elif test_type == testdata.wrong_json_format_post:
            self.assertIn(spec.resp_msg_key, resp)
            self.assertEqual(spec.post_json_missing_key_err_msg, resp["Message"])
            self.assertEqual(falcon.HTTP_400, result.status)
