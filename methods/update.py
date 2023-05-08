from sqlalchemy import Table
from sqlalchemy.orm import Session


def update_single(table: Table, db: Session, id: int, entity) -> bool:
    try:
        query = table.update().where(
            table.c['id'] == id).values(**dict(entity))
        db.execute(query)
        return True
    except:
        return False


def update_many(table: Table, db: Session, id_to_entity: dict) -> bool:
    ids = list(id_to_entity.keys())
    entities = list(id_to_entity.values())
    res = False
    for i in range(len(id_to_entity)):
        res = update_single(table, db, ids[i], entities[i])
    return res
