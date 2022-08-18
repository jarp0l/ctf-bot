import asyncpg, os
from quart import Quart
from threading import Thread
from dotenv import load_dotenv
from pathlib import Path  # For paths

app = Quart(__name__)

cwd = Path(__file__).parents[0]
cwd = str(cwd)
load_dotenv(cwd + "/../.env")

DB_URI = os.getenv("DATABASE_URL")


@app.route("/")
async def home():
    return "Bot is working!"


@app.route("/challenges")
async def challenges():
    query = """
    SELECT author_id, category, challenge_description
      FROM challenges
    """

    conn = await asyncpg.connect(DB_URI)
    result = await conn.fetch(query)
    await conn.close()

    if result == []:
        return "Empty result"

    return result


def web_server():
    app.run(host="0.0.0.0", port=1337)


def server():
    t = Thread(target=web_server)
    t.start()
