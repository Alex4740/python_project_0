"""  tcontainhis module api for my application """
from flask import Flask, request, jsonify

my_list = ["I love my dog", "I ate fish"]

app: Flask = Flask(__name__) # this argument lets the object know it should look for its information.

@app.route("/greeting", method=["GET"])
def hello_world():
    return "hello world!"

@app.route("/personal/<name>", method=["GET"])
def personal_greating(name: str):   # anything in parameter here passed as str.
    return f"Hello {name}!"


@app.route("/list/<index>", method=["GET"])
def get_phrase_from_list(index: str):
    global my_list
    return my_list[int(index)]


# @app.route("/list", method=["post"])




app.run()