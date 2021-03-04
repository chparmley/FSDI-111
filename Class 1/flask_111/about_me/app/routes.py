#!/user/bin/env python3
# -*- coding: utf8 -*-
"""Route Definitions"""
from flask import jsonify
# from app module import the app variable (object)
from about_me.app import app


@app.route('/aboutme')
def about(): 
    me = {
        "first_name": "Charles",
        "last_name": "Parmley",
        "hobby": "Rollerblading"
    }

    return jsonify(me)