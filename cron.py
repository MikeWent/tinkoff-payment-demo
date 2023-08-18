#!/usr/bin/env python3

from os import getenv
import logging

import tinkoff

logging.basicConfig(level=logging.DEBUG)

TERMINAL_KEY = getenv("TINKOFF_TERMINAL_KEY")
PASSWORD = getenv("TINKOFF_PASSWORD")

tink = tinkoff.TinkoffKassa(TERMINAL_KEY, PASSWORD)
payment_id = input("Enter payment id: ")
rebill_id = input("Enter rebill id (from notification): ")
print(tink.charge(payment_id, rebill_id))
