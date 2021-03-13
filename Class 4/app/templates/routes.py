from flask import render_template
from app import app, db
from app.database import User

@app.route("/about/<int:uid>")
def about(uid):
    user = User.query.filter_by(id=uid).first()
    return {
        "first_name" : user.first_name,
        "last_name" : user.last_name,
        "hobbies" : user.hobbies0
    }


@app.route("/user/<name>")
