from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, Integer

class CarbohydrateType(Base):
    __tablename__ = 'HIDRATOS_DE_CARBONO_TIPOS'
    IdTipoHidratoDeCarbono = Column(Integer, primary_key=True)
    Tipo = Column(Integer)
    Descripcion = Column(String)
    
    def __init__(self, idTipoHidratoDeCarbono, tipo, descripcion):
        self.IdTipoHidratoDeCarbono = idTipoHidratoDeCarbono
        self.Tipo = tipo
        self.Descripcion = descripcion
    
    def __repr__(self):
        return f"CarbohydrateType({self.IdTipoHidratoDeCarbono}, {self.Tipo}, {self.Descripcion})"
        
    def __str__(self):
        return self.CarbohydrateType
    
    def Create(tipo: int,
               descripcion: str):
        carbohydrateTypeToInsert = CarbohydrateType(None,tipo,descripcion)
        return carbohydrateTypeToInsert