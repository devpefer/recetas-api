from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, Integer

class FatType(Base):
    __tablename__ = 'GRASAS_TIPOS'
    IdTipoGrasa = Column(Integer, primary_key=True)
    Tipo = Column(Integer)
    Descripcion = Column(String)
    
    def __init__(self, idTipoGrasa, tipo, descripcion):
        self.IdTipoGrasa = idTipoGrasa
        self.Tipo = tipo
        self.Descripcion = descripcion
    
    def __repr__(self):
        return f"FatType({self.IdTipoGrasa}, {self.Tipo}, {self.Descripcion})"
        
    def __str__(self):
        return self.FatType
    
    def Create(tipo: str, descripcion: str):
        fatTypeToInsert = FatType(None,tipo,descripcion)
        return fatTypeToInsert