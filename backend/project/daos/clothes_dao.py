from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from entities import ClothesEntity
from models import Clothes
from exceptions import ClothesNotFoundException, ClothesAlreadyExists
from app import db


class ClothesDAO():

    def get(self, clothes_id: int):
        try:
            obj = Clothes.query.filter_by(id=clothes_id).one()
        except NoResultFound:
            raise ClothesNotFoundException(f"There are no clothes with id {clothes_id}")

        return self.build_entity_from_orm(obj)

    def delete(self, clothes_id: int):
        try:
            count = Clothes.query.filter_by(id=clothes_id).delete()
        except NoResultFound:
            db.session.rollback()
            raise ClothesNotFoundException(f"There are no clothes with id {clothes_id}")
        db.session.commit()

        return count == 1

    def post(self, clothes: ClothesEntity) -> ClothesEntity:
        obj = self.build_orm_from_entity(clothes)

        try:
            db.session.add(obj)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ClothesAlreadyExists(f'Clothes `{entity.pk}` already exists.')
        except SQLAlchemyError:
            db.session.rollback()
            raise

        return self.build_entity_from_orm(obj)

    def put(self, clothes: ClothesEntity) -> ClothesEntity:
        try:
            result = db.session.query(Clothes).filter_by(id=clothes.id).update(clothes)
        except SQLAlchemyError:
            db.session.rollback()
            raise
        if result:
            db.session.commit()
        else:
            raise ClothesNotFoundException
        return self.get(clothes.id)

    @staticmethod
    def build_entity_from_orm(orm: Clothes) -> ClothesEntity:
        return ClothesEntity(
            id=orm.id,
            name=orm.name,
            blob_path=orm.blob_path,
            color=orm.color,
            cloth_type=orm.cloth_type
        )

    @staticmethod
    def build_orm_from_entity(entity: ClothesEntity) -> Clothes:
        return Clothes(
            id=entity.id,
            name=entity.name,
            blob_path=entity.blob_path,
            color=entity.color,
            cloth_type=entity.cloth_type
        )
