from sqlalchemy import Table
from sqlalchemy.orm import Session


def insert_many(table: Table, db: Session, entities: list) -> bool:
    for entity in entities:
        insert_single(table, db, entity)


def insert_single(table: Table, db: Session, entity) -> bool:
    try:
        query = table.insert().values(**dict(entity))
        res = db.execute(query)
        return True
    except:
        return False
