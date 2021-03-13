#!/user/bin/env python3
# -*- coding: utf8 -*-
"""Route Definitions"""

# from app module import the app variable (object)
from about_me.app import app
from about_me.app.database import create, read, update, delete
from flask import request, render_template

@app.route('/')
def index(): 
    return render_template("index.html")


"""@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent"""
    
'''@app.route("/numsum/<int:num>")
def calcs(num):
    total= 0
    for i in range(num+1):
        total+=i
    return render_template("numsum.html", number = num, data=int(num*(num+1)/2))'''


@app.route('/aboutme')
def about(): 
    me = {
        "first_name": "Charles",
        "last_name": "Parmley",
        "hobby": "Rollerblading",
        "bio": "Just a dude who likes computers"
    }
    """return str(me)"""
    return render_template("about.html", about=me)
    




#-------------------------   OH CRUD   ------------------------
@app.route("/create", methods=["POST"])
def new_product():
    product_data = request.json
    new_id = create_new_product(
        product_data.get("title"),
        product_data.get("qty"),
        product_data.get("price"),
        product_data.get("active")
    )
    return{"ok": True, "message": "Success", "new_id": new_id}


@app.route('/read')
def show_products(): 
    inventory = read()
    return render_template("products.html", products = inventory)


@app.route("/udpate/<id>", methods=["PUT"])
def update_product():
    product_data = request.json
    data = update(int(id), product_data)
    return{"ok": True, "message": "Updated"}


@app.route("/delete/<id>", methods=["DELETE"])
def delete_product(id):
    data = delete(int(id))

    return{"ok": True, "message": "Deleted"}