from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World"

#pip install "fastapi[all]"
#uvicorn 1:app --reload
#http://127.0.0.1:8000