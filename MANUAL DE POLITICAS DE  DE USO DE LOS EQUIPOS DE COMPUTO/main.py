from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from database import engine, inicializar_bd
from models import Politica
import crud

app = FastAPI()
inicializar_bd()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    with Session(engine) as session:
        yield session

@app.get("/politicas")
def listar(db: Session = Depends(get_db)):
    return crud.listar_politicas(db)

@app.get("/politicas/{id}")
def leer(id: int, db: Session = Depends(get_db)):
    politica = crud.obtener_politica(db, id)
    if not politica:
        raise HTTPException(status_code=404, detail="No encontrada")
    return politica

@app.post("/politicas", status_code=201)
def crear(politica: Politica, db: Session = Depends(get_db)):
    return crud.crear_politica(db, politica)

@app.put("/politicas/{id}")
def actualizar(id: int, politica: Politica, db: Session = Depends(get_db)):
    p = crud.actualizar_politica(db, id, politica)
    if not p:
        raise HTTPException(status_code=404, detail="No encontrada")
    return p

@app.delete("/politicas/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    if not crud.eliminar_politica(db, id):
        raise HTTPException(status_code=404, detail="No encontrada")
    return {"mensaje": "Política eliminada"}