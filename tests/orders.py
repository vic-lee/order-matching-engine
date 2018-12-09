import falcon
import json
from order_resources import OrderResources

class Orders:
    def is_order_valid(self, req):
        trader_id_key = "traderId"
        order_key = "orders"
        order_symbol_key = "symbol"
        order_quantity_key = "quantity"
        order_type_key = "orderType"
        try:
            self.client_json = json.loads(req.stream.read())["data"]
            if self.client_json.keys() == [ trader_id_key, order_key ]:
                for item in self.client_json[order_key]:
                    if item.keys() != [
                        order_symbol_key,\
                        order_quantity_key,\
                        order_type_key\
                    ]:
                        error_msg = """order object is missing one of these attributes: symbol, quantity, orderType"""
                        self.client_json = {
                            "Message": error_msg
                        }
                        return False
                    else:
                        continue
                return True
            else:
                self.client_json = {"Message": "Missing key order or traderId" }
                return False
            return True
        except ValueError, e:
            self.client_json = {"Message": "Empty input"}
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
        validated = self.is_order_valid(req)
        if (validated):
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_400
        resp.body = json.dumps(self.client_json)
