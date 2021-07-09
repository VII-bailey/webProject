from flask import Flask
from flask import Flask, render_template, app
from utils.functions import create_app

# app = Flask(__name__)

app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def get_fav():
    return app.send_static_file('favicon.ico')


if __name__ == '__main__':
    app.run()
