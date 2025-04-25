from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url="postgres://postgres:4038@localhost:5432/generator",
        modules={"models":["models.user", "models.desing", "models.meeting"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )