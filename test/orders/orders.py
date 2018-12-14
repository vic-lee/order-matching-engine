import falcon
import json
from datetime import datetime
from orders.database import OrdersDatabase
import orders.spec as spec


orders_db = OrdersDatabase()

class Error(Exception):
    pass

class JsonKeyError(Error):
    def __init__(self):
        self.message = "Your data object is missing key `order` or `traderId`"

class OrderKeyError(Error):
    def __init__(self):
        self.message = "Order object is missing one of these attributes: "+\
                        "symbol, quantity, orderType"

class OrderResources:
    def is_order_valid(self, req):
        try:
            # self.client_json = json.loads(req.stream.read())["data"]
            self.client_json = json.loads(req.stream.read())
            if "data" not in self.client_json:
                raise JsonKeyError
            self.client_json = self.client_json["data"]
            if not all(k in self.client_json.keys() for k in spec.data_keys):
                raise JsonKeyError
            for item in self.client_json[spec.order_key]:
                if not all(k in item.keys() for k in spec.order_keys_on_init):
                    raise OrderKeyError
                else:
                    continue
            return True
        except JsonKeyError as e:
            self.client_json = { "Message": e.message }
            return False
        except OrderKeyError as e:
            self.client_json = { "Message": e.message }
            return False
        except ValueError:
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
                self.handle_get_trader_order(resp, trader_orders)

    def on_post(self, req, resp):
        validated = self.is_order_valid(req)
        if (validated):
            order_time_str = str(datetime.now())
            self.add_time_stamps_to_orders(order_time_str)
            orders_db.add_order(self.client_json)
            resp.status = falcon.HTTP_201
            resp.body = json.dumps({ spec.resp_msg_key : spec.post_success_resp_msg })
        else:
            resp.body = json.dumps(self.client_json)
            resp.status = falcon.HTTP_400

    def add_time_stamps_to_orders(self, time):
        for order in self.client_json[spec.order_key]:
            order[spec.order_time_key] = time
            order[spec.order_status_key] = spec.order_status_open
        # print(self.client_json)

    def handle_get_all_orders(self, resp):
        orders_history = orders_db.get_all_orders()
        resp.body = json.dumps(orders_history)
        resp.status = falcon.HTTP_200

    def handle_invalid_trader_order_req(self, resp):
        resp.body = json.dumps({
            spec.resp_msg_key : spec.req_trader_missing_err_msg
        })
        resp.status = falcon.HTTP_404

    def handle_get_trader_order(self, resp, trader_orders):
        resp.body = json.dumps(trader_orders)
        resp.status = falcon.HTTP_200
