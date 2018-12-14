'''
This is a pseudo database that houses API data on post.

Presumably this module would be replaced by a service
that connects to a real database.
'''
import orders.spec as spec

class OrdersDatabase:
    """
    `orders` structure:
    orders = {
        "<traderId>": {
            "orders": [
                {
                    "symbol",
                    "quantity",
                    "ordreType"
                }
                ...
            ]
        }
    }

    Each `traderId` key represents a unique trader; its value is an
    object containing its orders (each with attribute `symbol`,
    `quantity`, `orderType`).

    Query a trader by searching for keys in `orders`.
    If key doesn't exist, create a new traderId key-value pair.

    Note that `orders` is reset every time the API is restarted.
    """

    def __init__(self):
        self.orders = {}

    def add_order(self, new_order):
        current_trader_id = new_order[spec.trader_id_key]
        if current_trader_id not in self.orders:
            self.orders[current_trader_id] = {
                spec.order_key: []
            }

        for order in new_order[spec.order_key]:
            matched = self.match_orders(order[spec.order_symbol_key],\
                order[spec.order_quantity_key], order[spec.order_type_key])
            if matched:
                order = self.fill_order(order)

        self.orders[current_trader_id][spec.order_key].extend(\
            new_order[spec.order_key])

    def get_all_orders(self):
        if (self.orders == {}):
            return {"Message": "No order"}
        return self.orders

    def get_trader_order(self, id):
        if id not in self.orders:
            return None
        else:
            return {"data": self.orders[id][spec.order_key]}

    def match_orders(self, sym, quantity, type):
        '''
        There is an order match iff there exists
        an order in the system that satisfies:
        1. same symbol
        2. same quantity (assume no partial fulfillment allowed)
        3. opposite order type
        4. status == open
        '''
        for trader_id in self.orders:
            for order in self.orders[trader_id][spec.order_key]:
                if order[spec.order_symbol_key] == sym and\
                order[spec.order_quantity_key] == quantity and\
                order[spec.order_type_key] != type and\
                order[spec.order_status_key] == spec.order_status_open:
                    print("we found a match!")
                    order = self.fill_order(order)
                    return True
        return False

    def fill_order(self, order):
        order[spec.order_status_key] = spec.order_status_filled
        return order
