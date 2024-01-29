import datetime as dt
from decimal import Decimal
from pydantic import BaseModel, validator
from enum import Enum

from models.abstract import NatureEnum, SexEnum


class BaseEmpleado(BaseModel):
    naturaleza: NatureEnum 
    identificacion: str
    
    nombre:str
    apellido:str
    sexo: SexEnum
    
    fecha_nacimiento: dt.date
    fecha_contratacion: dt.date
    telefono: str 
    salario: Decimal
    

class CreateEmpleado(BaseEmpleado):
    naturaleza: NatureEnum = "V"
    foto: bytes | None = None
    telefono: str | None = None
    
    cargo_id: int
    departamento_id: int
    
    bonos: list[int] | None = None
    @validator("fecha_nacimiento", pre=True)
    def validate_fecha_nacimiento(cls, value):
        data = dt.datetime.strptime(value, "%d-%M-%Y")
        return data.date()
    
    @validator("fecha_contratacion", pre=True)
    def validate_fecha_contratacion(cls, value:str):
        data = dt.datetime.strptime(value, "%d-%M-%Y")
        return data.date()

class GetEmpleado(BaseEmpleado):
    naturaleza:NatureEnum
    foto: bytes | None = None
    
    # cargo
    # departamento
    class Config:
        orm_mode = True