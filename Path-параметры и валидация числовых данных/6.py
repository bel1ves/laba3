from enum import Enum

from fastapi import FastAPI


class Profile(str, Enum):
    name = "admin"
    password = "admin"


app = FastAPI()


@app.get("/")
async def get_model(name: str, password: str):
    if name != Profile.name:
        return "Wrong name"
    elif password != Profile.password:
        return "Wrong password"
    else:
        return "Accept"


# pip install "fastapi[all]"
# uvicorn 6:app --reload
# http://127.0.0.1:8000/?name=admin&password=adminn
# http://127.0.0.1:8000/?name=adminn&password=admin
# http://127.0.0.1:8000/?name=admin&password=admin
