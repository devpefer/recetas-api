from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, Integer, DECIMAL

class RelationshipFoodVitamin(Base):
    __tablename__ = 'RELACION_INGREDIENTES_VITAMINAS'
    IdIngrediente = Column(Integer, primary_key=True)
    IdVitamina = Column(Integer, primary_key=True)
    CantidadVitaminaEnIngrediente = Column(DECIMAL)
    PorCada = Column(DECIMAL)
    UnidadMedidaVitaminaEnIngrediente = Column(String)
    
    def __init__(self,idIngrediente, idVitamina, cantidadVitaminaEnIngrediente, porCada, unidadMedidaVitaminaEnIngrediente):
        self.IdIngrediente = idIngrediente
        self.IdVitamina = idVitamina
        self.CantidadVitaminaEnIngrediente = cantidadVitaminaEnIngrediente
        self.PorCada = porCada
        self.UnidadMedidaVitaminaEnIngrediente = unidadMedidaVitaminaEnIngrediente
    
    def __repr__(self):
        return f"RelationshipFoodVitamin({self.IdIngrediente}, {self.IdVitamina}, {self.CantidadVitaminaEnIngrediente}, {self.PorCada}, {self.UnidadMedidaVitaminaEnIngrediente})"
        
    def __str__(self):
        return self.RelationshipFoodVitamin
    
    def Create(foodID: int,
               vitaminID: int,
               vitaminInFood: float,
               each: float,
               unitOfMeasure: str):
        vitaminToInsert = RelationshipFoodVitamin(foodID,vitaminID,vitaminInFood,each,unitOfMeasure)
        return vitaminToInsert