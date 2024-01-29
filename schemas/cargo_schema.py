from pydantic import BaseModel

class CargoSchema(BaseModel):
    descripcion: str