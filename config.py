import os
API_ID = int("1311893")
API_HASH = os.getenv("9ee1ae5201d2af501d62f9b8f0cbf9b9")
BOT_TOKEN = os.getenv("5234613039:AAE-9giAYcDboJhcWJL8P8oTay35LQY3Imc")
DATABASE_URL = os.getenv("https://mamadmamadsong2.herokuapp.com/")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "592299058").split()})
