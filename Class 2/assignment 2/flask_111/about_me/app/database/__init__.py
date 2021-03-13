#!/user/bin/env python3
# -*- coding: utf8 -*-


from flask import g
from about_me.app import app
import sqlite3

DATABASE="user.db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Helper function to retrieve users
def get_all_users():
    # Retrieving the database cursor and executing a SQL command
    # The execute method below takes two parameters: a string with the query
    # and a tuple with values for a possible WHERE statement
    cursor = get_db().execute("SELECT * FROM user", ())
    # Returning all results from the previous query into a "results" variable
    results = cursor.fetchall()
    # Closing cursor connection to minimize thread use
    cursor.close()
    return results














def create(title,qty,price,active):
    some_var = (title,qty,price,active)
    command = """INSERT INTO product (title, qty, price, active) VALUES(?,?,?,?)"""
    cursor = get_db()
    last_row_id = cursor.execute(command, some_var).lastrowid
    cursor.commit()
    return last_row_id

def read():
    cursor = get_db().execute("SELECT * FROM product", ())
    results = cursor.fetchall()
    cursor.close()
    return results

def update(id, fields: dict):
    field_string = ", ".join(
                    "%s=\"%s\"" % (key, val)
                        for key, val
                        in fields.items())
    query = """
            UPDATE product
            SET %s
            WHERE id = ?
            """ % field_string
    cursor = get_db()
    cursor.execute(query, (prod_id,))
    cursor.commit()
    return True

def delete(prod_id):
    query = "DELETE FROM product WHERE id=%s" % prod_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True
    