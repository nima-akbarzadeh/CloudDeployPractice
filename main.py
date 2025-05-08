import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from library.wiki_summary import summarize

app = FastAPI()

class Wiki(BaseModel):
    name: str

@app.post("/summarize")
async def summarize_page(wiki: Wiki):
    result = summarize(wiki)
    payload = {"wikipedia": result}
    return JSONResponse(content=jsonable_encoder(payload))

@app.get("/")
async def root():
    return {"message": "Hello all!"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    return {"sum": num1 + num2}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)

