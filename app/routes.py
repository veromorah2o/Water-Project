from flask import Flask, render_template
from app import app


@app.route("/")
@app.route('/index')
def index():
    return render_template('home.html')


@app.route("/1D")
def one():
    return render_template('one_dimension.html')


@app.route("/2D")
def two():
    return render_template('two_dimension.html')
