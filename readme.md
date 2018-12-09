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
