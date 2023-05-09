from sqlalchemy import Table
from sqlalchemy.orm import Session


class ItemRepository:
    def __init__(self, table: Table, db: Session) -> None:
        self.table = table
        self.db = db

    def select(self, predicate):
        query = self.table.select()
        if predicate is not None:
            query = query.where(predicate)

        res = self.db.execute(query)
        return res

    def insert_single(self, entity_dict: dict) -> bool:
        try:
            query = self.table.insert().values(**entity_dict)
            self.db.execute(query)
            return True
        except:
            return False

    def insert_many(self, entities: list) -> bool:
        res = False
        for entity in entities:
            res = self.insert_single(dict(entity))
        return res

    def update_single(self, id: int, entity) -> bool:
        try:
            query = self.table.update().where(
                self.table.c['id'] == id).values(**dict(entity))
            self.db.execute(query)
            return True
        except:
            return False

    def update_many(self, id_to_entity: dict) -> bool:
        ids = list(id_to_entity.keys())
        entities = list(id_to_entity.values())
        res = False
        for i in range(len(id_to_entity)):
            res = self.update_single(ids[i], entities[i])
        return res

    def delete_single(self, item_id: int) -> bool:
        try:
            query = self.table.delete().where(self.table.c['id'] == item_id)
            self.db.execute(query)
            return True
        except:
            return False

    def delete_many(self, item_ids: list) -> bool:
        res = False
        for id in item_ids:
            res = self.delete_single(id)
        return res
