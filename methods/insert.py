from sqlalchemy import Table
from sqlalchemy.orm import Session


def insert_single(table: Table, db: Session, entity) -> bool:
    try:
        query = table.insert().values(**dict(entity))
        db.execute(query)
        return True
    except:
        return False


def insert_many(table: Table, db: Session, entities: list) -> bool:
    res = False
    for entity in entities:
        res = insert_single(table, db, entity)
    return res
