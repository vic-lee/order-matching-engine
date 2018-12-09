import falcon
import json
from order_resources import OrderResources

class Orders:
    def on_get(self, req, resp):
        sample_order_resp = {
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
        resp.body = json.dumps(sample_order_resp)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        if data is not None:
            output = data
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output)
        else:
            output = {
                "Message": "Please pass in input"
            }
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(output)
