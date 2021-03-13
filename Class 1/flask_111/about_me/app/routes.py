#!/user/bin/env python3
# -*- coding: utf8 -*-
"""Route Definitions"""
# from app module import the app variable (object)
from about_me.app import app


@app.route('/aboutme')
def about(): 
    me = {
        "first_name": "Charles",
        "last_name": "Parmley",
        "hobby": "Rollerblading"
    }

    return(me)