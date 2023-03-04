from src.Application.Carbohydrates.Commands.commands import Commands
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, Integer

class Carbohydrate(Base):
    __tablename__ = 'HIDRATOS_DE_CARBONO'
    IdHidratoDeCarbono = Column(Integer, primary_key=True)
    IdTipoHidratoDeCarbono = Column(Integer)
    NombreEspanyol = Column(String)
    NombreIngles = Column(String)
    NombreEuropeo = Column(String)
    DescripcionEspanyol = Column(String)
    DescripcionIngles = Column(String)
    
    def __init__(self,idHidratoDeCarbono, idTipoHidratoDeCarbono, nombreEspanyol, nombreIngles, nombreEuropeo, descripcionEspanyol, descripcionIngles):
        self.IdHidratoDeCarbono = idHidratoDeCarbono
        self.IdTipoHidratoDeCarbono = idTipoHidratoDeCarbono
        self.NombreEspanyol = nombreEspanyol
        self.NombreIngles = nombreIngles
        self.NombreEuropeo = nombreEuropeo
        self.DescripcionEspanyol = descripcionEspanyol
        self.DescripcionIngles = descripcionIngles
    
    def __repr__(self):
        return f"Carbohydrate({self.IdHidratoDeCarbono}, {self.IdTipoHidratoDeCarbono}, {self.NombreEspanyol}, {self.NombreIngles}, {self.NombreEuropeo}, {self.DescripcionEspanyol}, {self.DescripcionIngles})"
        
    def __str__(self):
        return self.Carbohydrate
    
    def Create(idTipoHidratoDeCarbono: int,
               nombreEspanyol: str,
               nombreIngles: str,
               nombreEuropeo: str,
               descripcionEspanyol: str,
               descripcionIngles: str):
        carbohydrateToInsert = Carbohydrate(None,idTipoHidratoDeCarbono,nombreEspanyol, nombreIngles, nombreEuropeo, descripcionEspanyol, descripcionIngles)
        return carbohydrateToInsert