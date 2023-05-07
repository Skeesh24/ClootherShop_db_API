from sqlalchemy import Table
from sqlalchemy.orm import Session


def update_single(table: Table, db: Session, id, entity) -> bool:
    try:
        query = table.update().where(
            table.c['id'] == id).values(**dict(entity))
        db.execute(query)
        return True
    except:
        return False
