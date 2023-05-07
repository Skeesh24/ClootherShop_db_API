from sqlalchemy import Table
from sqlalchemy.orm import Session


def select_all(table: Table, db: Session):
    query = table.select()
    return db.execute(query).all()


def count_all(table: Table, db: Session):
    return len(select_all(table, db))


def select_single(table: Table, db: Session, predicate):
    query = table.select().where(predicate)
    res = db.execute(query).first()
    return res
