## Questions

1. Is partial order allowed when matching orders?
    - Example:
      - incoming order: sell 100 AAPL shares (id=1)
      - current opening orders (in order of traversal):
        - 30 AAPL orders (id=2)
        - 90 AAPL orders (id=3)
      - orders result
        - order (id=1) closed
        - order (id=2) closed
        - order (id=3) breaks into 2 orders:
          - order (id=3.1): sell 70 AAPL shares, filled
          - order (id=3.2): sell 20 AAPL shares, open


## Endpoints documentation

In order to avoid misunderstanding of the challenge's Readme on my part, I have listed the endpoints according to my implementation.

| **Endpoint** | **Return value** |
| --- | --- |
|`/orders`| Returns all orders in the database, or an empty JSON if empty.<br>Please see `orders_db` for the structure of the pseudo-database.|
|`/orders/{trader_id}`| Returns all orders by a trader if `trader_id` is found in the database, or 404 if not found.|
