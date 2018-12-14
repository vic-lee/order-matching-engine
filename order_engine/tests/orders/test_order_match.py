import falcon

from tests.orders.test_order_classes import TestOrders
import tests.orders.test_orders_data as testdata
import orders.spec as spec

class TestOrdersMatching(TestOrders):
    def test_order_matching(self):
        self.order_matching_test_handler(testdata.order_matching_data)

    def order_matching_test_handler(self, payload):
        for p in payload:
            self.simulate_post(self.order_endpoint, json=p)

        result = self.simulate_get(self.order_endpoint)
        resp = result.json

        self.assertEqual(falcon.HTTP_200, result.status)

        for p in payload:
            trader_id = p[spec.data_key][spec.trader_id_key]
            self.assertEqual(spec.order_status_filled,\
             resp[trader_id][spec.order_key][0][spec.order_status_key])
