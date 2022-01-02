from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    return "welcome to the home page of FastAPI"

##http://127.0.0.1:8000/add?A=2&B=5
@app.get('/add')
def add(A,B):
    c=int(A)+int(B)
    return c

#http://127.0.0.1:8000/name?name=amiu&lname=tiwari
@app.get('/name')
def add(name,lname):
    c="my name is "+name+" "+lname
    return c


# @app.get("/items/")
# async def read_items(q: Optional[str] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

