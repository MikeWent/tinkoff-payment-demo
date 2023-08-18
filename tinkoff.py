from hashlib import sha256
import logging

import requests


class TinkoffKassa:
    base_url = "https://securepay.tinkoff.ru/v2/"
    terminal_key: str
    password: str

    def __init__(self, terminal_key: str, password: str) -> None:
        self.terminal_key = terminal_key
        self.password = password

    def _req(self, api_method: str, params: dict) -> dict:
        r = requests.post(
            url=self.base_url + api_method,
            json=self._sign(params),
        )
        logging.debug("request: %s" % r.request.body)
        logging.debug("response: %s" % r.text)
        return r.json()

    def _sign(self, params: dict) -> dict:
        params["TerminalKey"] = self.terminal_key
        params["Password"] = self.password

        root_only = dict()
        for k, v in params.items():
            if not isinstance(v, dict):
                root_only.update({k: v})
        sorted_by_key = sorted(root_only.items())
        concated_values = "".join([str(v) for k, v in sorted_by_key])
        token = sha256(concated_values.encode()).hexdigest()

        params["Token"] = token
        return params

    def init(
        self,
        amount: int,
        order_id: str,
        customer_key: str,
        notification_url: str | None = None,
        success_url: str | None = None,
        fail_url: str | None = None,
        recurrent: str = "Y",  # subscription
        pay_type: str = "O",  # one stage
    ):
        return self._req(
            "Init",
            params={
                "Amount": amount,
                "OrderId": order_id,
                "CustomerKey": customer_key,
                "NotificationURL": notification_url,
                "SuccessURL": success_url,
                "FailURL": fail_url,
                "Recurrent": recurrent,
                "PayType": pay_type,
            },
        )

    def get_state(self, payment_id: str):
        return self._req("GetState", params={"PaymentId": payment_id})

    def charge(self, payment_id: str, rebill_id: str) -> dict:
        return self._req(
            "Charge", params={"PaymentId": payment_id, "RebillId": rebill_id}
        )
