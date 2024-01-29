from config.backends import Base
from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy.sql import func
import enum

class BaseModel(Base):
    __abstract__ = True
    __tablename__:str = None
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True,)
    created_date = Column(DateTime, server_default=func.now())
    modified_date = Column(DateTime, onupdate=func.now())
    status = Column(Boolean, default=True)

class NatureEnum(str, enum.Enum):
    VENEZOLANO = "V"
    EXTRANJERO = "E"
    JURIDICO = "J"
    
class SexEnum(str, enum.Enum):
    MASCULINO = "M"
    FEMENINO = "F"