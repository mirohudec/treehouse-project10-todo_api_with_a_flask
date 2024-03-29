from flask import Flask, g, jsonify, render_template

import config
import models

from todo import todo_api


app = Flask(__name__)
app.register_blueprint(todo_api, url_prefix='/api/v1/')


@app.route('/')
def my_todos():
    return render_template('index.html')


if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
