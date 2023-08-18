import pytest

import tinkoff


@pytest.fixture
def tink() -> tinkoff.TinkoffKassa:
    # https://www.tinkoff.ru/kassa/dev/payments/#section/Podpis-zaprosa
    return tinkoff.TinkoffKassa("MerchantTerminalKey", "usaf8fw8fsw21g")
