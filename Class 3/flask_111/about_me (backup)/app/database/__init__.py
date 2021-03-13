#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Database functions"""

from flask import g
from about_me.app import app
import sqlite3

DATABASE = "inventory_manager.db"

# Establist Database connection
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Adding a new product
def create(name, price, quantity, description, category):
    values = (name, price, quantity, description, category)
    query = """INSERT INTO product(name, price, quantity, description, category) VALUES(?, ?, ?, ?, ?)"""
    cursor = get_db()
    last_row_id = cursor.execute(query, values).lastrowid
    cursor.commit()
    return last_row_id


# Retrieve all the current products
def get_all_products():
    cursor = get_db().execute("SELECT * FROM product", ())
    results = cursor.fetchall()
    cursor.close()
    return results


# Find a product by ID
def get_one_product(product_id):
    cursor = get_db().execute("SELECT * FROM product WHERE id = %s" % product_id, ())
    results = cursor.fetchall()
    cursor.close()
    return results


# Edit an existing user by ID
def update_product(product_id, values: dict):
    value_string = ",".join("%s=\"%s\"" % (key, val) for key, val in values.items())
    query = """UPDATE product SET %s WHERE id=?""" % value_string
    cursor = get_db()
    cursor.execute(query, (product_id))
    cursor.commit()
    return True


# Delete a product by ID
def delete_product(product_id):
    query = "UPDATE product SET active=0 WHERE id=%s" % product_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True


# Find all the inactive products
def get_inactive_products():
    cursor = get_db().execute("SELECT * FROM product WHERE active = 0")
    results = cursor.fetchall()
    cursor.close()
    return results


# Set a product to ac
def set_is_active(product_id):
    query = "UPDATE product SET active = 1 WHERE id = %s" % product_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True