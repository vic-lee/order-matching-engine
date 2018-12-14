'''
This file contains data for different test cases about /orders request.
'''

std_post = "STANDARD_POST_TEST"
wrong_json_format_post = "WORNG_JSON_FORMAT_POST"
non_numerical_quantity_post = "NON_NUMERICAL_QUANTITY_POST"

std_post_data = {
    "data":
    {
        "traderId": "skbks-sdk39sd-3ksfl43io3-alkjasf-34",
        "orders":
        [
            {
                "symbol": "AAPL",
                "quantity": 100,
                "orderType": "buy"
            },
            {
                "symbol": "NVDA",
                "quantity": 5000,
                "orderType": "buy"
            },
            {
                "symbol": "MSFT",
                "quantity": 2500,
                "orderType": "sell"
            }
        ]
    }
}

std_post_data_2 = {
    "data":
    {
        "traderId": "skbks-adfadee-3ksfl43io3-alkjasf-34",
        "orders":
        [
            {
                "symbol": "AAPL",
                "quantity": 100,
                "orderType": "buy"
            }
        ]
    }
}

std_post_data_3 = {
    "data":
    {
        "traderId": "skbks-adfadee-adgadfddd-alkjasf-34",
        "orders":
        [
            {
                "symbol": "BABA",
                "quantity": 100,
                "orderType": "sell"
            }
        ]
    }
}

order_matching_data = [
    {
        "data":
        {
            "traderId": "order_mathing_trader",
            "orders":
            [
                {
                    "symbol": "GOOG",
                    "quantity": 100,
                    "orderType": "sell"
                }
            ]
        }
    },
    {
        "data":
        {
            "traderId": "order_mathing_trader_2",
            "orders":
            [
                {
                    "symbol": "GOOG",
                    "quantity": 100,
                    "orderType": "buy"
                }
            ]
        }
    }
]

wrong_json_format_post_data = {
    "traderId": "skbks-sdk39sd-3ksfl43io3-alkjasf-34",
    "orders":
    [
        {
            "symbol": "AAPL",
            "quantity": 100,
            "orderType": "buy"
        },
        {
            "symbol": "NVDA",
            "quantity": 5000,
            "orderType": "buy"
        },
        {
            "symbol": "MSFT",
            "quantity": 2500,
            "orderType": "sell"
        }
    ]
}

non_numerical_quantity_post = {
    "traderId": "skbks-sdk39sd-3ksfl43io3-alkjasf-34",
    "orders":
    [
        {
            "symbol": "AAPL",
            "quantity": 100,
            "orderType": "buy"
        },
        {
            "symbol": "NVDA",
            "quantity": 5000,
            "orderType": "buy"
        },
        {
            "symbol": "MSFT",
            "quantity": 2500,
            "orderType": "sell"
        }
    ]
}
