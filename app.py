from flask import Flask

from ChildProject import food
from ChildProject.components import sorcery

app = Flask(__name__)


@app.route("/")
def hello_world():
    # http://127.0.0.1:5001/
    return "<p>This is another parent project</p>"


@app.route("/magic")
def get_magic():
    # http://127.0.0.1:5001/magic
    return sorcery.magic()


@app.route("/special")
def get_special():
    # http://127.0.0.1:5001/special
    return sorcery.special()


@app.route("/lunch")
def get_lunch():
    # http://127.0.0.1:5001/lunch
    return food.lunch()


@app.route("/dinner")
def get_dinner():
    # http://127.0.0.1:5001/dinner
    return food.dinner()


if __name__ == "__main__":
    app.run()
