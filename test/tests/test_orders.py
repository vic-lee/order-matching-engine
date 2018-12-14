import unittest
import json
from falcon import testing
import app


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
        docs = {
            "data":
            {
                "traderId": "skbks-sdk39sd-3ksfl43io3-alkjasf-34",
                "orders":
                [
                    {
                        "symbol": "AAPL",
                        "quantity": 100,
                        "orderType": "buy"
                    },
                    {
                        "symbol": "NVDA",
                        "quantity": 5000,
                        "orderType": "buy"
                    },
                    {
                        "symbol": "MSFT",
                        "quantity": 2500,
                        "orderType": "sell"
                    }
                ]
            }
        }
        headers = {"Content-Type": "application/json"}
        result = self.simulate_post('/orders', json=docs)
        resp = result.json
        assert "Message" in resp
        assert "Post successful" in resp["Message"]

# if __name__ == "__main__":
#     unittest.main()
