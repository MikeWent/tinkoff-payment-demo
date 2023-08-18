import tinkoff


def test_demo_sign(tink: tinkoff.TinkoffKassa):
    # https://www.tinkoff.ru/kassa/dev/payments/#section/Podpis-zaprosa
    demo_params = {
        "PaymentId": "2304882",
        "Amount": 19200,
        "Receipt": {
            "FfdVersion": "1.2",
            "ClientInfo": {},
            "Taxation": "osn",
            "Email": "a@test.ru",
            "Phone": 79031234567,
            "Customer": "Customer ID",
            "CustomerInn": "7777777777",
            "Items": [],
            "Payments": [],
        },
    }
    assert (
        tink._sign(demo_params)["Token"]
        == "d20308febb1c333c26d6b1e138d71d0be922475a97e69f41ee3eb0c525fa0f1c"
    )
