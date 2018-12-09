import falcon
import json
from order_resources import OrderResources
from orders_spec import trader_id_key, order_key,\
    order_symbol_key, order_quantity_key, order_type_key


order_resources = OrderResources()

class Orders:
    def is_order_valid(self, req):
        try:
            self.client_json = json.loads(req.stream.read())["data"]

            if set(self.client_json.keys()) == { trader_id_key, order_key }:
                for item in self.client_json[order_key]:
                    if set(item.keys()) != {
                        order_symbol_key,\
                        order_type_key,\
                        order_quantity_key\
                    }:
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
            order_resources.add_order(self.client_json)
        else:
            resp.status = falcon.HTTP_400
        resp.body = json.dumps(self.client_json)
