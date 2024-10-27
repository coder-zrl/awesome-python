# coding: utf-8

from flask import Flask, render_template
import flask

app = Flask(__name__)  # type: Flask
app.debug = True

@app.route('/')
def login():
    context = {
        "user": {
            "name": "Warren",
            "age": -18,
            "gender": None,
            "comment": u'<script>alert("弹出框")</script>'}
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
