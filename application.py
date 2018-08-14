import os

from flask_socketio import SocketIO, emit
from flask import Flask, session , request ,render_template , flash , redirect , url_for , session , logging

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()