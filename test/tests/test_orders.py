import unittest
import json
from falcon import testing, falcon

import app
import tests.test_orders_data as testdata

class TestOrders(testing.TestCase):
    def setUp(self):
        super(TestOrders, self).setUp()
        self.app = app.create()

class TestOrderCreation(TestOrders):

    def test_get_message(self):
        result = self.simulate_get('/orders')
        # for individual_resp in resp:
            # assert "orders" in individual_resp


    def test_post_order(self):
        docs = testdata.std_post_data
        result = self.simulate_post('/orders', json=docs)
        resp = result.json

        assert "Message" in resp
        assert "Post successful" in resp["Message"]
        assert falcon.HTTP_201 == result.status

# if __name__ == "__main__":
#     unittest.main()
