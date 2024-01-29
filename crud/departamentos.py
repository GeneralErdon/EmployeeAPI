
from models.empleados_models import Departamento
from utils.utils import BaseCRUD


class DepartamentoCrud(BaseCRUD):
    db_model = Departamento