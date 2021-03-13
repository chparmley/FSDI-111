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

def add_user():
    command = '''INSERT INTO user("first_name", "last_name", "hobby", "bio") VALUES(?, ?, ?, ?);'''

    fname = input('First Name: ')
    lname = input('Last Name: ')
    hobby = input('Hobby: ')
    bio = input('Bio: ')

    data = fname, lname, hobby, bio

    cursor = get_db.execute(command, data)

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