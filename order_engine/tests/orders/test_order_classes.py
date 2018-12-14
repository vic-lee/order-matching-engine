import unittest
import json
from falcon import testing, falcon

import app
import tests.orders.test_orders_data as testdata
import orders.spec as spec

class TestBase(testing.TestCase):
    def setUp(self):
        super(TestBase, self).setUp()
        self.app = app.create()

    def assertOrderExists(self, order_sent, server_orders):
        order_list = []
        for order in server_orders:
            server_order_init_format = {
                spec.order_symbol_key: order[spec.order_symbol_key],
                spec.order_quantity_key: order[spec.order_quantity_key],
                spec.order_type_key: order[spec.order_type_key],
            }
            order_list.append(server_order_init_format)
        if order_sent not in order_list:
            raise AssertionError("Order " + str(order_sent) + " is not found on server")

class TestOrders(TestBase):
    order_endpoint = '/orders'



# if __name__ == "__main__":
#     unittest.main()
