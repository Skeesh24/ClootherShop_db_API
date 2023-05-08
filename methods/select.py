from sqlalchemy import Table
from sqlalchemy.orm import Session


def select_where(table: Table, db: Session, predicate):
    query = table.select().where(predicate)
    res = db.execute(query)
    return res


def select_all(table: Table, db: Session):
    query = table.select()
    return db.execute(query).all()
