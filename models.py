from sqlalchemy import Column, Integer, String, Float
from database import Base

class Participante(Base):
    __tablename__ = "participantes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer)
    cidade = Column(String)

class Pontuacao(Base):
    __tablename__ = "pontuacoes"
    id = Column(Integer, primary_key=True, index=True)
    participante_id = Column(Integer)
    tentativas = Column(Integer)
    pontuacao = Column(Float)
