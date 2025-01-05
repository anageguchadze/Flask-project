from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '<p>Hello, Ana!</p>'

from markupsafe import escape

@app.route('/<name>')
def hello(name):
    return f"Hello, {escape(name)}!"