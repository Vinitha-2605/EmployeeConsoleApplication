import os
from dotenv import load_dotenv
load_dotenv()


def config():
    db_config = {"host": os.getenv("host"), "user": os.getenv("user"),
                 "password": os.getenv("password"), "database": os.getenv("database")}
    return db_config
