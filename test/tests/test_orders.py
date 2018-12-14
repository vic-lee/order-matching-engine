import unittest
from falcon import testing
import app


class TestOrders(testing.TestCase):
    def setUp(self):
        super(TestOrders, self).setUp()
        self.app = app.create()

class TestOrderCreation(TestOrders):
    def test_get_message(self):
        doc = {"Message": "No order"}
        result = self.simulate_get('/orders')
        print(doc)
        print(result)
        self.assertEqual(result.json, doc)

# if __name__ == "__main__":
#     unittest.main()
