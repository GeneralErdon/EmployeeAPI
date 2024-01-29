from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, Query
from sqlalchemy.exc import IntegrityError
from crud.departamentos import DepartamentoCrud
from models.empleados_models import Departamento
from config.backends import get_db
from schemas.departamento_schema import DepartamentoSchema
from utils.utils import obj_exists

departamento_router = APIRouter(prefix="/departamento")


@departamento_router.get("/")
def get_list(skip:int=0, limit:int=100, db:Session = Depends(get_db)):
    crud = DepartamentoCrud()
    data: Query[Departamento] = crud.list(db, skip, limit)
    obj_exists(db, data, many=True, raise_404=True)
    
    return data.all()

@departamento_router.get("/{departamento_id}")
def get_object(departamento_id:int, db:Session = Depends(get_db)):
    crud = DepartamentoCrud()
    departamento_obj:Departamento | None = crud.retrieve(db, departamento_id)
    obj_exists(db, departamento_obj, raise_404=True)
    
    return departamento_obj

@departamento_router.post("/")
def create_object(schema:DepartamentoSchema, db:Session = Depends(get_db)):
    crud = DepartamentoCrud()
    try:
        departamento_obj = crud.create(db, schema)
    except IntegrityError:
        return JSONResponse({
            "error": "Ya existe un registro con ese nombre"
        }, status_code=status.HTTP_403_FORBIDDEN)
    
    return JSONResponse({
        "message": "Objeto creado exitosamente",
        "object": schema.model_dump()
    }, status_code=status.HTTP_201_CREATED)