from flask import render_template

from app import app



@app.route('/')
def index():
    """
    :return: The template of the index website
    """
    return render_template("index.html")
