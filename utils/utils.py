from pathlib import Path
from typing import Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session, Query
from pydantic import BaseModel

BASE_DIR = Path().resolve()


def obj_exists(
    db: Session, data: Any | Query[Any], many: bool = False, raise_404: bool = False
):
    if many:
        ...
        if not db.query(data.exists()).scalar():
            if raise_404:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No se han encontrado resultados",
                )
            return False
        return True
    if data is None:
        if raise_404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No encontró el objeto",
            )
        return False
    
    return True


class BaseCRUD:
    db_model: Any

    def filter_by_id(self, db: Session, obj_id: int) -> Query[Any]:
        return db.query(self.db_model).filter(self.db_model.id == obj_id)

    def list(self, db: Session, skip: int = 0, limit: int = 100) -> Query[Any]:
        data_qs = db.query(self.db_model).offset(skip).limit(limit)
        return data_qs

    def retrieve(self, db: Session, obj_id: int) -> Any | None:
        data = self.filter_by_id(db, obj_id).first()
        return data

    def create(self, db: Session, schema: BaseModel) -> Any:
        data = schema.model_dump(exclude_unset=True)
        db_obj = self.db_model(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, obj_id: int, schema: BaseModel):
        data = schema.model_dump(exclude_unset=True)
        obj_qs = self.filter_by_id(db, obj_id)
        updated: int = obj_qs.update(data, synchronize_session=False)

        db.commit()
        db.refresh(obj_qs.first())
        return updated

    def delete(self, db: Session, obj_id: Any) -> bool:
        obj_qs = self.filter_by_id(db, obj_id)
        obj_qs.update({"status": False}, synchronize_session=False)
        db.commit()
