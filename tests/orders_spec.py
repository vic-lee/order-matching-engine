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

def trader_id_key():
    return "traderId"

def order_key():
    return "orders"

def order_symbol_key():
    return "symbol"

def order_quantity_key():
    return "quantity"

def order_type_key():
    return "orderType"
