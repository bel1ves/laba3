from enum import Enum

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

class Profile(str, Enum):
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")

    name = "admin"
    password = "admin"


app = FastAPI()


@app.get("/")
async def get_model(name: str | None = "", password: str | None = ""):
    if name != Profile.name:
        return "Wrong name"
    elif password != Profile.password:
        return "Wrong password"
    else:
        return "Accept"

# pip install "fastapi[all]"
# uvicorn 8:app --reload
# http://127.0.0.1:8000/?password=adminn
# http://127.0.0.1:8000/?name=admin
# http://127.0.0.1:8000/?name=admin&password=adminn
# http://127.0.0.1:8000/?name=admin&password=admin

