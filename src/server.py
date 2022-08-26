from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is working!"


def web_server():
    app.run(host="0.0.0.0", port=1337)


def server_thread():
    t = Thread(target=web_server)
    t.start()
