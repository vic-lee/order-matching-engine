import falcon
from health_check import HealthCheck
from orders import OrderResources

APP = falcon.API()

health_check_resource = HealthCheck()

APP.add_route('/health', health_check_resource)
APP.add_route('/orders', OrderResources())
