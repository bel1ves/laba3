from datetime import datetime, time, timedelta
from enum import Enum
from typing import Set, List, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


class ProgrammLanguage():
    Name: str = ""
    Librarys: Set[str] = []

    def __init__(self, name, librarys):
        self.Name = name
        self.Librarys = librarys


class Profile(str, Enum):
    Name = "admin"
    Password = "admin"
    Languages: Set[str] = Field(examples=["English", "Russian", "German"])
    ProgrammLanguages: Set[ProgrammLanguage] = Field(examples=[ProgrammLanguage("Python", ["fastapi", "tkinter"])])
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "Name": "admin",
                    "Password": "admin",
                    "Languages": ["English", "Russian", "German"],
                    "ProgrammLanguages": [ProgrammLanguage("Python", ["fastapi", "tkinter"])],
                }
            ]
        }
    }


profile = Profile

app = FastAPI()


@app.get("/")
async def get_model(name: str | None = "", password: str | None = "", timeEnter=datetime.now()):
    if name != profile.Name:
        return "Wrong name"
    elif password != profile.Password:
        return "Wrong password"
    else:
        results = {"Name": profile.Name, "Languages": profile.Languages, "ProgrammLanguages": profile.ProgrammLanguages,
                   "TimeEnter": timeEnter}
        return results

# pip install "fastapi[all]"
# uvicorn 11:app --reload
# http://127.0.0.1:8000/?name=admin&password=admin
