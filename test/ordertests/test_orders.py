import falcon
import pytest
from ordersystem.app import APP
from falcon import testing

@pytest.fixture
def client():
    return testing.TestClient(APP)

def test_list_images(client):
    doc = {
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
    response = client.simulate_get('/orders')

    assert response.json == doc
    assert response.status == falcon.HTTP_OK
