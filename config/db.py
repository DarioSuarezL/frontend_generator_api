from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
import os


def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url=os.getenv("DB_URL"),
        modules={"models": ["models.user", "models.meeting"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
