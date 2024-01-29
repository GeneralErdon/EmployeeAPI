from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from sqlalchemy.orm import Session
from config.backends import get_db
from crud.cargos import CargoCrud
from models.empleados_models import Cargo
from schemas.cargo_schema import CargoSchema

cargo_router = APIRouter(prefix="/cargo")

@cargo_router.get("/")
def list_cargos(skip:int = 0, limit:int = 100, db:Session = Depends(get_db)):
    crud = CargoCrud()
    data = crud.list(db, skip, limit)
    if not db.query(data.exists()).scalar():
        raise HTTPException(status.HTTP_404_NOT_FOUND, "No se ha encontrado cargos")
    return data.all()

@cargo_router.get("/{cargo_id}")
def retrieve_cargo(cargo_id:int, db:Session = Depends(get_db)):
    crud = CargoCrud()
    cargo_obj: Cargo = crud.retrieve(db, cargo_id)
    if not cargo_obj:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "No se ha enconrtrado el cargo con id %s" % cargo_id)
    return cargo_obj


@cargo_router.post("/")
def create_cargo(schema:CargoSchema, db:Session = Depends(get_db)):
    crud = CargoCrud()
    obj = crud.create(db, schema)
    return obj

@cargo_router.put("/{cargo_id}")
def update_cargo(cargo_id:int, schema:CargoSchema, db:Session = Depends(get_db)):
    crud = CargoCrud()
    cargo_obj = crud.retrieve(db, cargo_id)
    if cargo_obj is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "No se ha encontrado")
    crud.update(db, cargo_id, schema)
    
    return JSONResponse({
        "message": "Se ha actualizado correctamente el objeto"
    }, status_code=status.HTTP_200_OK)


@cargo_router.delete("/{cargo_id}")
def delete(cargo_id:int, db:Session=Depends(get_db)):
    crud = CargoCrud()
    
    cargo_obj = crud.retrieve(db, cargo_id)
    if cargo_obj is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "No se ha encontrado")
    
    crud.delete(db, cargo_id)
    return JSONResponse({
        "message": "Se ha Desactivado correctamente el objeto"
    }, status_code=status.HTTP_200_OK)