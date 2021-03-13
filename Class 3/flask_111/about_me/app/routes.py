#!/user/bin/env python3
# -*- coding: utf8 -*-
"""Route Definitions"""

# from app module import the app variable (object)
from about_me.app import app
from about_me.app.database import get_all_products, get_inactive_products, delete_product, set_is_active, get_one_product
from flask import redirect, request, render_template


# ---- I N D E X
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Adding a new product
@app.route("/product/add", methods=["POST"])
def add_product():
    data = request.json
    new_product = create(
        data.get("name"),
        data.get("price"),
        data.get("quantity"),
        data.get("description"),
        data.get("category")
    )

    return {"ok": True, "message": "Success", "product": new_product}


# Edit an existing product by ID
@app.route("/product/<product_id>/edit", methods=["PUT"])
def edit_product(product_id):
    data = request.json
    out = update_product(product_id, data)
    return {"ok": out, "message": "Updated"}


# Retrieve all the current products
@app.route("/products")
def all_products():
    out = get_all_products()
    return render_template("products.html", products = out)

# Find a product by ID
@app.route("/product/<product_id>")
def one_product(product_id):
    find_product = get_one_product(product_id)
    return render_template("find_product.html", find_product = find_product)


# Delete a product by ID
@app.route("/product/<product_id>/remove", methods=["GET"])
def remove_product(product_id):
    out = delete_product(product_id)
    return redirect("/products")



# Find all the inactive products
@app.route("/products/inactive")
def inactive_products():
    out = get_inactive_products()
    return render_template("/inactive.html", products = out)


# Set a product to active
@app.route("/product/<product_id>/activate")
def activate_product(product_id):
    out = set_is_active(product_id)
    return redirect("/products/inactive")

# Error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("Error.html"), 404
