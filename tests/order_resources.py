class OrderResources:
    # data model for orders, arranged by traders
    # {
    #       "traderId": String
    #       "orders":
    #       [
    #           "symbol": String
    #           "quantity": Integer
    #           "orderType": String
    #       ]
    # }
    orders = {}     # dict of each trader's orders
