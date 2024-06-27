from fastapi import FastAPI

app = FastAPI()

# if (name == null):
Name: str = "Name"


@app.get("/users/me")
async def read_user_me():
    return f"user name: {Name}"


@app.get("/users/{name}")
async def read_user(name: str):
    Name = name
    return f"new user name: {Name}"

# pip install "fastapi[all]"
# uvicorn 3:app --reload
# http://127.0.0.1:8000/users/me
# Вариант с сохранением не работает
# http://127.0.0.1:8000/users/mee
