from models.empleados_models import Cargo
from utils import BaseCRUD

class CargoCrud(BaseCRUD):
    db_model = Cargo