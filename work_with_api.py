from os import getenv

import pybase64
import requests


def get_all_orders():
    auth_byte_string = bytes(
        f'{getenv("MOYSKLAD_USER")}:{getenv("MOYSKLAD_PASS")}',
        "utf-8"
    )
    auth_encode_string = pybase64.b64encode_as_string(auth_byte_string)

    url = getenv("MOYSKLAD_URL")
    headers = {"Authorization": f"Basic {auth_encode_string}"}

    request_orders = requests.get(url, headers=headers).json()
    orders = request_orders.get("rows")
    return orders