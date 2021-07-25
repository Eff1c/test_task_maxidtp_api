import datetime
import uuid

import work_with_db


def add_item_to_db(order):
    # check if there is an entry with this id in db
    result_query = work_with_db.check_unique_order(order)
    if result_query:
        # check identity (necessary update or no)
        if identity_check(result_query, order):
            work_with_db.update_order(order)
            return "Updated"
        
        return "No changes"

    else:
        work_with_db.insert_new_order(order)
        return "Created"


def get_orders_last_week(all_orders):
    week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    # generator for faster executions
    return [
        order for order in all_orders if datetime.datetime.fromisoformat(order["created"]) >  week_ago
    ]


def identity_check(result_query, order):
    # if record has been updated (in api service)
    # we get only one record
    # [1:] - reject id field
    return result_query[0][1:] != (
        order["sum"],
        order["name"],
        order["created"]
    )
    

def is_valid_uuid(val):
    try:
        return uuid.UUID(str(val))
    except ValueError:
        return None


def save_orders_in_db(orders):
    for order in orders:
        # convert str to datetime
        if type(order["created"]) == str:
            order["created"] = datetime.datetime.fromisoformat(
                order["created"]
            )
        # if order["created"] is NoneType or other than type str
        else:
            order["created"] = None

        add_item_to_db(order)
