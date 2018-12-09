import falcon
from health_check import HealthCheck
from orders  import Orders

APP = falcon.API()

health_check_resource = HealthCheck()
sample_orders = Orders()
APP.add_route('/health', health_check_resource)
APP.add_route('/orders', sample_orders)
