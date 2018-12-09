"""
This file defines the keys in order data model as constants.

data model for orders, arranged by traders
{
   "traderId": String
   "orders":
   [
       "symbol": String
       "quantity": Integer
       "orderType": String
  ]
}
"""

trader_id_key = "traderId"

order_key = "orders"

order_symbol_key = "symbol"

order_quantity_key = "quantity"

order_type_key = "orderType"

data_keys = [trader_id_key, order_key]

order_keys = [order_symbol_key, order_quantity_key, order_type_key]


# def trader_id_key():
#     return "traderId"
#
# def order_key():
#     return "orders"
#
# def order_symbol_key():
#     return "symbol"
#
# def order_quantity_key():
#     return "quantity"
#
# def order_type_key():
#     return "orderType"
