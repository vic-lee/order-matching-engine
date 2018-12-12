import falcon
from health_check import HealthCheck
from orders.orders import OrderResources

APP = falcon.API()

health_check_resource = HealthCheck()
order_resources = OrderResources()

APP.add_route('/health', health_check_resource)
APP.add_route('/orders', order_resources)
