from fastapi import FastAPI

app = FastAPI()


@app.get("/{name}")
async def read_item(name: str):
    return f"Name {name}"

#pip install "fastapi[all]"
#uvicorn 2:app --reload
#http://127.0.0.1:8000/items/3