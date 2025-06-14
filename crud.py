from sqlalchemy.orm import Session
from models import Participante, Pontuacao

def criar_participante(db: Session, nome: str, idade: int, cidade: str):
    novo = Participante(nome=nome, idade=idade, cidade=cidade)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def registrar_pontuacao(db: Session, participante_id: int, tentativas: int, pontuacao: float):
    ponto = Pontuacao(participante_id=participante_id, tentativas=tentativas, pontuacao=pontuacao)
    db.add(ponto)
    db.commit()
    db.refresh(ponto)
    return ponto

def obter_historico(db: Session, participante_id: int):
    return db.query(Pontuacao).filter(Pontuacao.participante_id == participante_id).all()
