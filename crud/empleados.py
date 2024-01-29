from sqlalchemy.orm import Session
from models.empleados_models import Empleado
from utils.utils import BaseCRUD

class EmpleadoCrud(BaseCRUD):
    db_model = Empleado