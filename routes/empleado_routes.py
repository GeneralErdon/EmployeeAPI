from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, Query
from config.backends import get_db
from crud.empleados import EmpleadoCrud
from models.empleados_models import Empleado
from schemas.empleados_schemas import CreateEmpleado, GetEmpleado
from utils.utils import obj_exists


empleados_router = APIRouter(prefix="/empleado")


@empleados_router.get("/", response_model=GetEmpleado)
async def get_list(skip:int = 0, limit:int = 100, db:Session = Depends(get_db)):
    crud = EmpleadoCrud()
    data:Query[Empleado] = crud.list(db, skip, limit)
    obj_exists(db, data, many=True, raise_404=True)
    
    return data.all()

@empleados_router.get("/{empleado_id}")
async def get_empleado(empleado_id:int, db:Session = Depends(get_db)):
    crud = EmpleadoCrud()
    empleado_obj: Empleado | None = crud.retrieve(db, empleado_id)
    # empleado_obj = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    
    if not empleado_obj:
        raise HTTPException(
                status.HTTP_404_NOT_FOUND, 
                {"error_msg": "El empleado con id %s no se ha encontrado" % empleado_id}
            )
    return empleado_obj

@empleados_router.post("/")
async def create_empleado(empleado_schema:CreateEmpleado, db:Session = Depends(get_db)):
    crud = EmpleadoCrud()
    obj:Empleado = crud.create(db, empleado_schema)
    
    return obj