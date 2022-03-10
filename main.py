""" this module is to my api application"""

from flask import Flask, request, jsonify

app: Flask = Flask(__name__)

@app.route("/greeting", method=["GET"])
def hello_world():
    return "hello world!"


app.run()

