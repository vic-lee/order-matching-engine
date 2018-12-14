# Order Matching Engine API

## Table of contents

- [Project structure](#project-structure)
- [Endpoints documentation](#endpoints-documentation)
- [Testing the APIs](#testing-the-apis)
  - [Running tests](#running-tests)
  - [On handler functions](#on-handler-functions)
  - [Test cases](#test-cases)
- [Assumptions made in implementation](#assumptions-made-in-implementation)

## Project structure

```
|-- order_engine
    |-- app.py
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

- `orders/orders.py` implements functions that handle Post and Get requests at the `/orders` endpoint.
- `orders/database.py` implements a local data storage structure for API posts and requests.
- `orders/spec.py` contains static variables about keys in the JSON data structure and is used throughout the project.

Details on tests and their implementation can be found in the [Testing the APIs](#testing-the-apis) section.

## Endpoints documentation

The following table lists all endpoints available.

| **Endpoint** | **Methods** | **Return value** |
| --- | --- | --- |
|`/orders`| `GET` `POST` |Returns all orders in the database, or an empty JSON if empty.<br><br>You may also post a trader's orders using this endpoint.<br><br>Please see `orders/database.py` for the structure of the pseudo-database.|
|`/orders/{trader_id}`| `GET` |Returns all orders by a trader if `trader_id` is found in the database, or 404 if not found.|

## Testing the APIs


The tests of this program is written using python's `unittest` framework. Tests on GET, POST, and the matching process are written. Specifically, `test_order_classes.py` defines the base test class for testing orders. `test_order_data.py` contains test data for different test cases in test files. The other `test_order_*` files are test files.

The structure of the tests is reproduced below:

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

### On handler functions

Each test file contains `*_handler` functions that handles each test case. For instance, the following code snippet in `test_order_get.py` calls `get_order_test_handler` to test if the API successfully returns orders associated with a trader ID:

```python
payload = testdata.std_post_data
tid = testdata.std_post_data[spec.data_key][spec.trader_id_key]
self.get_order_test_handler(payload=payload, trader_id=tid)
```

`*_handler` functions are essentially wrapper functions on various assert statements that I've created to make each test case more readable. Each `*_handler` function call is a test case. Since `*_handler` functions are only called in `test_*` functions, the list of `*_handler` functions called represent all the test cases.

### Test cases
- tests on `GET`
  - if successfully gets all orders in database
  - if successfully gets a trader's orders in database
- tests on `POST`
  - if successfully posts in database
  - if successfully blocks post requests with mistakes in JSON format
- tests on Order matching
  - if orders are matched

## Assumptions made in implementation

I have assumed that partially filled orders are not allowed in this system, based on my understanding of the requirements. That is, the state of an order is binary: it's either `filled` or `open`. Also, it is impossible to partition a big order into 2 smaller order (no overlaps), with one filled and the other open.

Since I'm not sure if "partially filled order" is a term that is used in practice, the following is an example of what I mean by this term:

```
- Example:
  - incoming order: sell 100 AAPL shares (id=1)
  - current opening orders (in order of traversal):
    - 30 AAPL orders (id=2)
    - 90 AAPL orders (id=3)
  - orders result
    - order (id=1) closed
    - order (id=2) closed
    - order (id=3) partitioned into 2 orders:
      - order (id=3.1): sell 70 AAPL shares, filled
      - order (id=3.2): sell 20 AAPL shares, open
```
