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
