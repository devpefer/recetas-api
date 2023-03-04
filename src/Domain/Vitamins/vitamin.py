from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, Integer

class Vitamin(Base):
    __tablename__ = 'VITAMINAS'
    IdVitamina = Column(Integer, primary_key=True)
    IdCategoriaVitamina = Column(Integer)
    NombreVitaminaEspanyol = Column(String)
    NombreVitaminaIngles = Column(String)
    NombreVitaminaEuropeo = Column(String)
    DescripcionVitaminaEspanyol = Column(String)
    DescripcionVitaminaIngles = Column(String)
    
    def __init__(self,idVitamina,
                 idCategoriaVitamina,
                 nombreEspanyol,
                 nombreIngles,
                 nombreEuropeo,
                 descripcionEspanyol,
                 descripcionIngles):
        
        self.IdVitamina = idVitamina
        self.IdCategoriaVitamina = idCategoriaVitamina
        self.NombreVitaminaEspanyol = nombreEspanyol
        self.NombreVitaminaIngles = nombreIngles
        self.NombreVitaminaEuropeo = nombreEuropeo
        self.DescripcionVitaminaEspanyol = descripcionEspanyol
        self.DescripcionVitaminaIngles = descripcionIngles
    
    def __repr__(self):
        return f"Vitamina({self.IdVitamina}, "\
                            f"{self.IdCategoriaVitamina}, "\
                            f"{self.NombreVitaminaEspanyol}, "\
                            f"{self.NombreVitaminaIngles}, "\
                            f"{self.NombreVitaminaEuropeo}, "\
                            f"{self.DescripcionVitaminaEspanyol}, "\
                            f"{self.DescripcionVitaminaIngles})"
        
    def __str__(self):
        return self.Vitamina
    
    def Create(idCategoriaVitamina: int,
               nombreEspanyol: str,
               nombreIngles: str,
               nombreEuropeo: str,
               descripcionEspanyol: str,
               descripcionIngles: str):
        
        return Vitamin(None,idCategoriaVitamina,
                       nombreEspanyol,
                       nombreIngles,
                       nombreEuropeo,
                       descripcionEspanyol,
                       descripcionIngles)
        