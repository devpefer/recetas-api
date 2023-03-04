from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, Integer

class Fat(Base):
    __tablename__ = 'GRASAS'
    IdGrasa = Column(Integer, primary_key=True)
    IdTipoGrasa = Column(Integer)
    NombreEspanyol = Column(String)
    NombreIngles = Column(String)
    NombreEuropeo = Column(String)
    DescripcionEspanyol = Column(String)
    DescripcionIngles = Column(String)
    
    def __init__(self,idGrasa, idTipoGrasa, nombreEspanyol, nombreIngles, nombreEuropeo, descripcionEspanyol, descripcionIngles):
        self.IdGrasa = idGrasa
        self.IdTipoGrasa = idTipoGrasa
        self.NombreEspanyol = nombreEspanyol
        self.NombreIngles = nombreIngles
        self.NombreEuropeo = nombreEuropeo
        self.DescripcionEspanyol = descripcionEspanyol
        self.DescripcionIngles = descripcionIngles
    
    def __repr__(self):
        return f"Fat({self.IdGrasa}, {self.IdTipoGrasa}, {self.NombreEspanyol}, {self.NombreIngles}, {self.NombreEuropeo}, {self.DescripcionEspanyol}, {self.DescripcionIngles})"
        
    def __str__(self):
        return self.Fat
    
    def Create(idTipoGrasa: int,
               nombreEspanyol: str,
               nombreIngles: str,
               nombreEuropeo: str,
               descripcionEspanyol: str,
               descripcionIngles: str):
        fatToInsert = Fat(None,idTipoGrasa,nombreEspanyol,nombreIngles,nombreEuropeo,descripcionEspanyol,descripcionIngles)
        return fatToInsert