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