#!/user/bin/env python3
# -*- coding: utf8 -*-
"""Route Definitions"""

# from app module import the app variable (object)
from about_me.app import app


@app.route('/')
def index(): 
    dictionary = {
        "first_name": "Charles",
        "last_name": "Parmley",
        "hobby": "Rollerblading"
    }

    return dictionary



if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")