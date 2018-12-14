# Order Matching Engine API

## Project structure

```
|-- order_engine
    |-- orders
        | -- database.py
        | -- orders.py       
        | -- spec.py
    |-- tests
        |-- orders
            |-- test_order_classes.py
            |-- test_order_get.py
            |-- test_order_match.py
            |-- test_order_post.py
            |-- test_order_data.py
```

- `orders/orders.py` has the main logic that handles incoming API requests.
- `orders/database.py` implements a local data storage structure for API posts and requests.
- `orders/spec.py` contains static variables about keys in the JSON data structure and is used throughout the project.

## Endpoints documentation

The following table lists all endpoints available.

| **Endpoint** | **Methods** | **Return value** |
| --- | --- | --- |
|`/orders`| `GET` `POST` |Returns all orders in the database, or an empty JSON if empty.<br><br>You may also post a trader's orders using this endpoint.<br><br>Please see `orders/database.py` for the structure of the pseudo-database.|
|`/orders/{trader_id}`| `GET` |Returns all orders by a trader if `trader_id` is found in the database, or 404 if not found.|

## Testing the APIs

The tests of this program is written using python's `unittest` framework. Tests on GET, POST, and the matching process are written. There is also a separate file that houses test data as well as another that declares the base test class.

```
|-- order_engine
    |-- tests
        |-- orders
            |-- test_order_classes.py
            |-- test_order_get.py
            |-- test_order_match.py
            |-- test_order_post.py
            |-- test_order_data.py
```
### Running tests

To run a test, run the following commands:
```console
> cd order_engine
> python3 -m unittest tests/orders/name_of_the_test.py
```


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
