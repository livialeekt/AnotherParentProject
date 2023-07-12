from flask import Flask

from ChildProject import food
from ChildProject.components import sorcery

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>This is another parent project</p>"


@app.route("/magic")
def get_magic():
    return sorcery.magic()


@app.route("/magic")
def get_special():
    return sorcery.special()


@app.route("/lunch")
def get_lunch():
    return food.lunch()


@app.route("/dinner")
def get_dinner():
    return food.dinner()


if __name__ == "__main__":
    app.run()
