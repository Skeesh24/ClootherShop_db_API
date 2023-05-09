from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from services.repository import ItemRepository
from classes.items import ItemRequest, items, Item, ItemResponse
from utils.database import get_db
from methods.responses import details
from methods.mapping import keyvalue_map


app = FastAPI()


@app.get("/")
def root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
def item_by_id(item_id: int, db: Session = Depends(get_db)):
    # need a codes: 400, 401, 403
    rep = ItemRepository(items, db)

    res = rep.select(items.c['id'] == item_id).first()

    if res is not None:
        return JSONResponse(keyvalue_map(Item, res), status_code=200)
    else:
        return JSONResponse(details("an elem was not found"), status_code=404)


@app.get("/items")
def items_all(db: Session = Depends(get_db)):
    rep = ItemRepository(items, db)

    res = rep.select(None)
    response = [keyvalue_map(Item, x) for x in res]

    if res is not None:
        return JSONResponse(response, status_code=200)
    else:
        return JSONResponse(details("there is an empty sequence for ur request"), status_code=404)


@app.post("/items")
def insert_item(item: ItemRequest, db: Session = Depends(get_db)):
    try:
        new_item = Item(**dict(item))
        new_dic = dict(zip(list(new_item.__dict__.keys())[
                       1:], list(new_item.__dict__.values())[1:]))
        rep = ItemRepository(items, db)

        rep.insert_single(new_dic)

        db.commit()

        index = len(rep.select_all())+1
        dict_response = ItemResponse(id=index, **new_dic).__dict__

        return JSONResponse(dict_response, status_code=201)
    except Exception as e:  # terminate an except msg before posting
        return JSONResponse(details(f"have a nice day! {e}"), status_code=500)


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemRequest, db: Session = Depends(get_db)):
    rep = ItemRepository(items, db)

    old_item = rep.select_where(items.c['id'] == item_id).first()
    if old_item is None:
        return JSONResponse(details("not found"), status_code=404)

    dict_response = ItemResponse(id=item_id, **dict(item)).__dict__

    success = rep.update_single(item_id, item)
    db.commit()

    if success:
        return JSONResponse(dict_response, status_code=202)
    else:
        return JSONResponse(details("sorry, we have a mistake at the server-side"), status_code=500)


@app.delete("/items/{item_id}")
def delete_item(item_id, db: Session = Depends(get_db)):
    rep = ItemRepository(items, db)

    old_item = rep.select_where(items.c['id'] == item_id).first()
    if old_item is None:
        return JSONResponse(details("not found"), status_code=404)

    success = rep.delete_single(item_id)
    db.commit()

    if success:
        return JSONResponse(details("No content"), status_code=204)
    else:
        return JSONResponse(details("sorry, we have a mistake at the server-side"), status_code=500)
