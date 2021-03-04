#!/user/bin/env python3
# -*- coding: utf8 -*-
"""Route Definitions"""

# from app module import the app variable (object)
from about_me.app import app
from about_me.app.database import get_all_users

@app.route('/')
def index(): 
    return "Hello, world!"

@app.route('/aboutme')
def about(): 
    me = {
        "first_name": "Charles",
        "last_name": "Parmley",
        "hobby": "Rollerblading",
        "bio": "Just a dude who likes computers"
    }
    return str(me)


@app.route('/users')
def scan_users(): 
    out = get_all_users()
    return str(out)