from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI

load_dotenv(find_dotenv())

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
