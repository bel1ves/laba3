from enum import Enum

from fastapi import FastAPI



app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return f"file_path {file_path}"

# pip install "fastapi[all]"
# uvicorn 5:app --reload
# http://127.0.0.1:8000/http://127.0.0.1:8000/models/resnet
