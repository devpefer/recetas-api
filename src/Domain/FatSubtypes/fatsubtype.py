from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, Integer

class FatSubtype(Base):
    __tablename__ = 'GRASAS_SUBTIPOS'
    IdSubtipoGrasa = Column(Integer, primary_key=True)
    IdTipoGrasa = Column(Integer)
    Subtipo = Column(Integer)
    Descripcion = Column(String)
    
    def __init__(self,idSubtipoGrasa, idTipoGrasa, subtipo, descripcion):
        self.IdSubtipoGrasa = idSubtipoGrasa
        self.IdTipoGrasa = idTipoGrasa
        self.Subtipo = subtipo
        self.Descripcion = descripcion
    
    def __repr__(self):
        return f"FatSubtype({self.IdSubtipoGrasa}, {self.IdTipoGrasa}, {self.Subtipo}, {self.Descripcion})"
        
    def __str__(self):
        return self.FatSubtype
    
    def Create(fatSubtypeID: str, subtype: str, description: str):
        fatSubtypeToInsert = FatSubtype(None,fatSubtypeID,subtype,description)
        return fatSubtypeToInsert