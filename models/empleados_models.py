from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, String, ForeignKey, Enum, Date,
    DECIMAL, Boolean, Table
    )
from models.abstract import BaseModel, NatureEnum, SexEnum





class Departamento(BaseModel):
    __tablename__ = "departamento"
    
    descripcion = Column(String(100), unique=True)
    empleados = relationship("Empleado", back_populates="departamento")


class Cargo(BaseModel):
    __tablename__ = "cargo"
    
    descripcion = Column(String(100), unique=True)
    empleados = relationship("Empleado", back_populates="cargo")

empleado_bono_association = Table(
    'empleado_bono',
    BaseModel.metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True,),
    Column("bono_id", Integer, ForeignKey("bono.id")),
    Column("empleado_id", Integer, ForeignKey("empleado.id"))
)

class Bono(BaseModel):
    __tablename__ = "bono"
    #
    monto_usd = Column(DECIMAL(100, 2), default=0.0)
    monto_bs = Column(DECIMAL(100, 2), default=0.0)
    aplica_arreglo = Column(Boolean, default=False)
    empleados = relationship("Empleado", secondary=empleado_bono_association, back_populates="bonos")




class Empleado(BaseModel):
    __tablename__ = "empleado"
    # Personal identification
    naturaleza = Column(Enum(NatureEnum), index=True, default="V")
    identificacion = Column(String(14), unique=True, index=True,)
    
    nombre = Column(String)
    apellido = Column(String)
    sexo = Column(Enum(SexEnum), default="M",)
    # Personal data
    fecha_nacimiento = Column(Date)
    fecha_contratacion = Column(Date)
    
    telefono = Column(String, nullable=True)
    foto = Column(String, nullable=True, ) # Crearle un manager de insercion de imagenes
    salario = Column(DECIMAL(100, 2), default=0.0)
    
    # Foreign Keys
    cargo_id = Column(Integer, ForeignKey("cargo.id",))
    cargo = relationship("Cargo", back_populates="empleados")
    departamento_id = Column(Integer, ForeignKey("departamento.id", ))
    departamento = relationship("Departamento", back_populates="empleados")
    bonos = relationship("Bono", secondary=empleado_bono_association, back_populates="empleados")
    