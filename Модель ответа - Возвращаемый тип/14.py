from datetime import datetime, time, timedelta
from enum import Enum
from typing import Set, List, Union, Any

from fastapi import Body, FastAPI, Cookie, Header
from pydantic import BaseModel, Field
from typing_extensions import Annotated

app = FastAPI()


class ProgrammLanguage():
    Name: str = ""
    Librarys: Set[str] = []

    def __init__(self, name, librarys):
        self.Name = name
        self.Librarys = librarys


class Profile(BaseModel):
    Name: str = "admin"
    Password: str = "admin"


profiles = [Profile(Name="Jim", Password="12345"),
            Profile(Name="Lux", Password="qwerty")]


@app.post("/items/")
async def create_profile(profile: Profile) -> Profile:
    return profile


@app.get("/items/")
async def read_profiles() -> list[Profile]:
    return profiles

    # pip install "fastapi[all]"
    # uvicorn 14:app --reload
    # http://127.0.0.1:8000/items/
