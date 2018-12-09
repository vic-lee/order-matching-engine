import falcon
import json
from order_resources import OrderResources

class Orders:
    def __validate_client_json(self, req):
        try:
            self.client_json = json.loads(req.stream.read())
            return True
        except ValueError, e:
            self.client_json = {"Message": "Invalid input"}
            return False

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
        validated = self.__validate_client_json(req)
        if (validated):
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_400
        resp.body = json.dumps(self.client_json)
