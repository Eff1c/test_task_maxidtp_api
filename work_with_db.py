import pymssql
from os import getenv


def get_db_conn(func):
    def wrap(*args, **kwargs):
        with pymssql.connect(
            getenv("DATABASE_SERVER"),
            getenv("DATABASE_USER"),
            getenv("DATABASE_PASSWORD"),
            getenv("DATABASE_NAME"),
        ) as conn:
            cursor = conn.cursor()
            output = func(cursor=cursor, *args, **kwargs)
            conn.commit()
        
        return output
    return wrap


@get_db_conn
def check_unique_order(order, cursor):
    # if order already exists
    cursor.execute(
        "SELECT * FROM illia_orders WHERE id=%s",
        order["id"]
    )
    result_query = cursor.fetchall()
    return result_query


@get_db_conn
def update_order(order, cursor):
    cursor.execute(
        """
        UPDATE illia_orders
        SET sum=%d, name=%s, created=%s
        WHERE id=%s
        """,
        (
            order["sum"],
            order["name"],
            order["created"],
            order["id"]
        )
    )


@get_db_conn
def insert_new_order(order, cursor):
    cursor.execute(
        "INSERT INTO illia_orders (id, sum, name, created) VALUES (%s, %d, %s, %s)",
        (
            order["id"],
            order["sum"],
            order["name"],
            order["created"]
        )
    )
