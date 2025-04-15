from typing import Union

from fastapi import FastAPI,Depends
from database import get_db,Base,engine
from sqlalchemy.orm import Session
from routes import user
from models import usermodels
app = FastAPI()


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user.router,prefix='/auth',tags=['Authentication'])
@app.get('/testing')
def test(db:Session=Depends(get_db)):
    return {"HEy Dubey"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}