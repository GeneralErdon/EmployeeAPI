from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from config.backends import get_db
from models.empleados_models import Empleado
from routes.cargo_routes import cargo_router
from routes.empleado_routes import empleados_router
from routes.departamento_routes import departamento_router

app = FastAPI()

app.include_router(empleados_router)
app.include_router(cargo_router)
app.include_router(departamento_router)