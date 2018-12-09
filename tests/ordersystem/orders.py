import falcon
import json

class Orders:
    def on_get(self, request, response):
        sample_order_response = {
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
        response.body = json.dumps(sample_order_response)
        response.status = falcon.HTTP_200
