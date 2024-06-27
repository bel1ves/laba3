from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Profile(BaseModel):
    Name: str
    Password: str


profiles = [
    {"Name": "Jim", "Password": "12345"},
    {"Name": "Lux", "Password": "qwerty"},
]


@app.get("/items/", response_model=list[Profile])
async def read_profiles():
    return profiles

# pip install "fastapi[all]"
# uvicorn 15:app --reload
# http://127.0.0.1:8000/items/
