import datetime

from flask import request
from flask_api import FlaskAPI, status

import additional_funcs
import work_with_api

# Create Flask app
app = FlaskAPI(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        # if input data not have at least 2 args (id and sum)
        if len(request.data) < 2:
            return {"Output": "Error! Please input data."}

        id = request.data.get("id")
        sum = request.data.get("sum")
        name = request.data.get("name")
        created = request.data.get("created")

        if not additional_funcs.is_valid_uuid(id):
            return {"Output": "Error! Please input valid uuid."}

        try:
            sum = float(sum)
        except (ValueError, TypeError):
            return {"Output": "Error! Please input valid sum."}

        try:
            if created is not None:
                # convert str to datetime
                created = datetime.datetime.fromisoformat(
                    created
                )
        except (ValueError, TypeError):
            return {"Output": "Error! Please input valid created datetime."}

        order = {
            "id": id,
            "sum": sum,
            "name": name,
            "created": created
        }

        output = additional_funcs.add_item_to_db(order)

        return {"Output": output}

    # request.method == 'GET'

    return {
        "id": "some uniqueidentifier",
        "sum": 00.0,
        "name": "example",
        "created": "2021-01-01 00:00:00.000",
        }


@app.route("/update_orders", methods=["GET"])
def update_orders():
    all_orders = work_with_api.get_all_orders()
    orders_last_week = additional_funcs.get_orders_last_week(all_orders)
    additional_funcs.save_orders_in_db(orders_last_week)
    return {"Output": "Successfully"}
