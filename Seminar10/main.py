from typing import Optional

from fastapi import FastAPI

# install: pip install fastapi uvicorn
# run: uvicorn main:app
# provides docs here: http://127.0.0.1:8000/docs
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
