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

data_key = "data"
trader_id_key = "traderId"
order_key = "orders"
order_symbol_key = "symbol"
order_quantity_key = "quantity"
order_type_key = "orderType"
order_time_key = "orderTime"
order_status_key = "status"
order_status_open = "open"
order_status_filled = "filled"

data_keys = [trader_id_key, order_key]
order_keys = [\
    order_symbol_key, order_quantity_key,\
    order_type_key, order_status_key, order_time_key\
]
order_keys_on_init = [order_symbol_key, order_quantity_key, order_type_key]

resp_msg_key = "Message"
empty_db_msg = "No order"
post_success_resp_msg = "Post successful"
post_json_missing_key_err_msg = "Your data object is missing key `order` or `traderId`"
req_trader_missing_err_msg = "The trader you requested does not exist"
