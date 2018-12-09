from orders_spec import trader_id_key, order_key,\
    order_symbol_key, order_quantity_key, order_type_key

class OrderResources:

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
    """

    def __init__(self):
        self.orders = {}

    def add_order(self, new_order):
        current_trader_id = new_order[trader_id_key]
        if current_trader_id not in self.orders:
            self.orders[current_trader_id] = {
                order_key: []
            }
        self.orders[current_trader_id][order_key].extend(\
            new_order[order_key])

    def get_all_orders(self):
        return self.orders;
