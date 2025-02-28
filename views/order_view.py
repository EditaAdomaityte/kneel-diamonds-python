import sqlite3
import json


def list_orders():
    # Open a connection to the database:
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = (
            sqlite3.Row
        )  # it tells Python how to format data and makes it readable
        db_cursor = (
            conn.cursor()
        )  # database assistant, sends commands to database, helps to look at one row at the time and provides methods to retrieve data

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """SELECT
                          o.id,
                          o.metal_id,
                          o.size_id,
                          o.style_id,
                          o.type_id
                          FROM Orders o
            """
        )  # """ for multiple line string"
        query_results = db_cursor.fetchall()

        orders = []
        for row in query_results:
            orders.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_orders = json.dumps(
            orders
        )  # converts python dictionaries into json strings, makes data ready for HTTP response
    return serialized_orders

def single_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = (
            sqlite3.Row
        )  # it tells Python how to format data and makes it readable
        db_cursor = (
            conn.cursor()
        )  # database assistant, sends commands to database, helps to look at one row at the time and provides methods to retrieve data
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.type_id
        FROM Orders o
        WHERE o.id = ?
        """, (pk,))
        query_results = db_cursor.fetchone()

        # Serialize Python list to JSON encoded string
        serialized_order = json.dumps(dict(query_results))
    return serialized_order

