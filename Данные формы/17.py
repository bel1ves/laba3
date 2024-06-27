from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

# pip install "fastapi[all]"
# uvicorn 17:app --reload
# http://127.0.0.1:8000/items/