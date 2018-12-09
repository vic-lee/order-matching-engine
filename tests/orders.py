import falcon
import json
from orders_db import OrdersDatabase
from orders_spec import trader_id_key, order_key,\
    order_symbol_key, order_quantity_key, order_type_key


orders_db = OrdersDatabase()

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
        except ValueError, e:
            self.client_json = {"Message": "Empty input"}
            return False

    def on_get(self, req, resp):
        req_trader_id = req.get_param("trader_id")
        if (req_trader_id is None):
            self.handle_get_all_orders(resp)
        else:
            trader_orders = orders_db.get_trader_order(req_trader_id)
            if trader_orders is None:
                self.handle_invalid_trader_order_req(resp)
            else:
                self.handle_trader_order(resp, trader_orders)


    def on_post(self, req, resp):
        validated = self.is_order_valid(req)
        if (validated):
            orders_db.add_order(self.client_json)
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({ "Message": "Post successful" })
        else:
            resp.body = json.dumps(self.client_json)
            resp.status = falcon.HTTP_400

    def handle_get_all_orders(self, resp):
        orders_history = orders_db.get_all_orders()
        resp.body = json.dumps(orders_history)
        resp.status = falcon.HTTP_200

    def handle_invalid_trader_order_req(self, resp):
        resp.body = json.dumps({ "Message": "The trader you requested does not exist"})
        resp.status = falcon.HTTP_404

    def handle_trader_order(self, resp, trader_orders):
        resp.body = json.dumps(trader_orders)
        resp.status = falcon.HTTP_200
