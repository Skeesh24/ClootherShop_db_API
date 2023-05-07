from sqlalchemy import Table
from sqlalchemy.orm import Session


def delete_single(table: Table, db: Session, item_id: int) -> bool:
    try:
        query = table.delete().where(table.c['id'] == item_id)
        db.execute(query)
        return True
    except:
        return False
