from sqlmodel import Session, select
from models import Politica

def listar_politicas(db: Session):
    return db.exec(select(Politica)).all()

def crear_politica(db: Session, politica: Politica):
    db.add(politica)
    db.commit()
    db.refresh(politica)
    return politica

def obtener_politica(db: Session, id: int):
    return db.get(Politica, id)

def actualizar_politica(db: Session, id: int, datos: Politica):
    politica = db.get(Politica, id)
    if politica:
        politica.titulo = datos.titulo
        politica.descripcion = datos.descripcion
        politica.categoria = datos.categoria
        db.commit()
        db.refresh(politica)
        return politica
    return None

def eliminar_politica(db: Session, id: int):
    politica = db.get(Politica, id)
    if politica:
        db.delete(politica)
        db.commit()
        return True
    return False