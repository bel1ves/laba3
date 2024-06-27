from enum import Enum

from fastapi import FastAPI


class Profile(str, Enum):
    name = "admin"
    password = "admin"


app = FastAPI()


@app.get("/{name}/{password}")
async def get_model(name: str, password: str):
    if name != Profile.name:
        return "Wrong name"
    elif password != Profile.password:
        return "Wrong password"
    else:
        return "Accept"

# pip install "fastapi[all]"
# uvicorn 4:app --reload
# http://127.0.0.1:8000/admin/adminn
# http://127.0.0.1:8000/adminn/admin
# http://127.0.0.1:8000/admin/admin
