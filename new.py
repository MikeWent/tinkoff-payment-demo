#!/usr/bin/env python3

from os import getenv
import logging

import tinkoff
from random import randint

logging.basicConfig(level=logging.DEBUG)

TERMINAL_KEY = getenv("TINKOFF_TERMINAL_KEY")
PASSWORD = getenv("TINKOFF_PASSWORD")

tink = tinkoff.TinkoffKassa(TERMINAL_KEY, PASSWORD)
n = randint(1000, 9999)
new_invoice = tink.init(
    amount=n,  # 10 rub -> 1000
    order_id=f"podpiska_{n}",
    customer_key=f"client_{n}",
    success_url="https://http.cat/200",
    fail_url="https://http.cat/402",
)

if new_invoice["Success"]:
    print()
    print("Go pay here:", new_invoice["PaymentURL"])
    print()

input("Then press enter.")
tink.get_state(new_invoice["PaymentId"])
