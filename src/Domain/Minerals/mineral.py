from src.Application.Minerals.Commands.commands import Commands
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, Integer

class Mineral(Base):
    __tablename__ = 'MINERALES'
    IdMineral = Column(Integer, primary_key=True)
    IdCategoriaMineral = Column(Integer)
    NombreMineralEspanyol = Column(String)
    NombreMineralIngles = Column(String)
    NombreMineralEuropeo = Column(String)
    DescripcionMineralEspanyol = Column(String)
    DescripcionMineralIngles = Column(String)
    
    def __init__(self,idMineral,
                 idCategoriaMineral,
                 nombreEspanyol,
                 nombreIngles,
                 nombreEuropeo,
                 descripcionEspanyol,
                 descripcionIngles):
        
        self.IdMineral = idMineral
        self.IdCategoriaMineral = idCategoriaMineral
        self.NombreMineralEspanyol = nombreEspanyol
        self.NombreMineralIngles = nombreIngles
        self.NombreMineralEuropeo = nombreEuropeo
        self.DescripcionMineralEspanyol = descripcionEspanyol
        self.DescripcionMineralIngles = descripcionIngles
    
    def __repr__(self):
        return f"Mineral({self.IdMineral}, "\
                            f"{self.IdCategoriaMineral}, "\
                            f"{self.NombreMineralEspanyol}, "\
                            f"{self.NombreMineralIngles}, "\
                            f"{self.NombreMineralEuropeo}, "\
                            f"{self.DescripcionMineralEspanyol}, "\
                            f"{self.DescripcionMineralIngles})"
        
    def __str__(self):
        return self.Mineral
    
    def Create(idCategoriaMineral: int,
               nombreEspanyol: str,
               nombreIngles: str,
               nombreEuropeo: str,
               descripcionEspanyol: str,
               descripcionIngles: str):
        
        return Mineral(None,idCategoriaMineral,
                       nombreEspanyol,
                       nombreIngles,
                       nombreEuropeo,
                       descripcionEspanyol,
                       descripcionIngles)
        