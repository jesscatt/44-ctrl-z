from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models, ia_module
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/participante/")
def criar_participante(nome: str, idade: int, cidade: str, db: Session = Depends(get_db)):
    return crud.criar_participante(db, nome, idade, cidade)

@app.post("/pontuar/")
def pontuar(participante_id: int, tentativas: int, pontuacao: float, db: Session = Depends(get_db)):
    return crud.registrar_pontuacao(db, participante_id, tentativas, pontuacao)

@app.get("/prever/")
def prever(participante_id: int, db: Session = Depends(get_db)):
    historico = crud.obter_historico(db, participante_id)
    dados = [{"tentativas": h.tentativas, "pontuacao": h.pontuacao} for h in historico]
    predicao = ia_module.prever_pontuacao(dados)
    return {"previsao_proxima_pontuacao": round(predicao, 2)}
