from sqlmodel import SQLModel, Field

class Politica(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    titulo: str
    descripcion: str
    categoria: str