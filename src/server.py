#!/bin/env python3
import os
from flask import Flask, render_template
from threading import Thread
from dotenv import load_dotenv
from pathlib import Path  # For paths
from sqlalchemy import create_engine, text

cwd = Path(__file__).parents[0]
cwd = str(cwd)
load_dotenv(cwd + "/../.env")

DB_URI = os.getenv("DATABASE_URL")
engine = create_engine(DB_URI, pool_size=5, pool_recycle=3600)
retrieve_challenges = text(
    """
  SELECT m.server_nickname, c.added_on, challenge_id, category, challenge_description FROM challenges as c, members as m WHERE c.author_id=m.member_id;
  """
)

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is working!"


@app.route("/challenges")
def challenges():
    with engine.connect() as conn:
        challenges = conn.execute(retrieve_challenges)
    return render_template("challenges.html", challenges=challenges)


def web_server():
    try:
        app.run(host="0.0.0.0", port=1337)
    except:
        app.run(host="0.0.0.0", port=1338)


def server_thread():
    t = Thread(target=web_server)
    t.start()


if __name__ == "__main__":
    web_server()
