import os
API_ID = int("1309660")
API_HASH = os.getenv("ba9dcff03638149081fc19693a43d600")
BOT_TOKEN = os.getenv("5234613039:AAE-9giAYcDboJhcWJL8P8oTay35LQY3Imc")
DATABASE_URL = os.getenv("https://mamadmamadsong2.herokuapp.com/")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "592299058").split()})
