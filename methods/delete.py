from sqlalchemy import Table
from sqlalchemy.orm import Session


def delete_single(table: Table, db: Session, item_id: int) -> bool:
    try:
        query = table.delete().where(table.c['id'] == item_id)
        db.execute(query)
        return True
    except:
        return False


def delete_many(table: Table, db: Session, item_ids: list) -> bool:
    res = False
    for id in item_ids:
        res = delete_single(table, db, id)
    return res
