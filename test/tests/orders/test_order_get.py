import falcon

from tests.orders.test_order_classes import TestOrders
import tests.orders.test_orders_data as testdata
import orders.spec as spec


class TestOrdersGet(TestOrders):

    def test_get_order(self):
        self.get_order_test_handler(\
            testdata.std_post_data,\
            testdata.std_post_data[spec.data_key][spec.trader_id_key])

        multiple_post_payload = [testdata.std_post_data,\
            testdata.std_post_data_2, testdata.std_post_data_3]

        self.get_order_test_handler(multiple_post_payload)


    def get_order_test_handler(self, payload, trader_id=None):
        if (type(payload) == list):
            for p in payload:
                self.simulate_post('/orders', json=p)
        else:
            self.simulate_post('/orders', json=payload)

        if trader_id == None:
            self.handle_get_all_trade_orders(payload)
        else:
            self.handle_get_trader_order(trader_id, \
                payload[spec.data_key][spec.order_key])


    def handle_get_trader_order(self, trader_id, data_sent):
        param = {"trader_id": trader_id}
        result = self.simulate_get(self.order_endpoint, params=param)
        resp = result.json
        self.assertEqual(falcon.HTTP_200, result.status)
        self.assertIn(spec.data_key, resp)
        for order in data_sent:
            self.assertOrderExists(order, resp[spec.data_key])


    def handle_get_all_trade_orders(self, data_sent):
        result = self.simulate_get(self.order_endpoint)
        resp = result.json
        self.assertEqual(falcon.HTTP_200, result.status)
        if spec.data_key not in resp:
            '''Expect getting order data from multiple traders'''
            for payload in data_sent:
                trader_id = payload[spec.data_key][spec.trader_id_key]
                for order in payload[spec.data_key][spec.order_key]:
                    self.assertOrderExists(order, resp[trader_id][spec.order_key])
        else:
            '''Expect getting data from one trading account'''
            for order_item in data_sent:
                self.assertOrderExists(order_item, resp[spec.data_key])
