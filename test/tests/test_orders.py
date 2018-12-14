from falcon import testing
import app


class TestOrders(testing.TestCase):
    def setUp(self):
        super(TestOrders, self).setUp()
        self.app = app.create()

class TestOrderCreation(TestOrders):
    def test_get_message(self):
        doc = {u'message': u'Hello world!'}

        result = self.simulate_get('/orders')
        self.assertEqual(result.json, doc)
