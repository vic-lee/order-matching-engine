import falcon
from health_check import HealthCheck
from orders.orders import OrderResources


health_check_resource = HealthCheck()
order_resources = OrderResources()

def create():
    api = falcon.API()
    api.add_route('/health', health_check_resource)
    api.add_route('/orders', order_resources)
    return api

APP = create()
