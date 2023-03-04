from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, Integer, DECIMAL

class RelationshipFoodCarbohydrate(Base):
    __tablename__ = 'RELACION_INGREDIENTES_HIDRATOS_DE_CARBONO'
    IdIngrediente = Column(Integer, primary_key=True)
    IdHidratoDeCarbono = Column(Integer, primary_key=True)
    CantidadHidratoDeCarbonoEnIngrediente = Column(DECIMAL)
    PorCada = Column(DECIMAL)
    UnidadMedidaHidratoDeCarbonoEnIngrediente = Column(String)
    
    def __init__(self,idIngrediente, idHidratoDeCarbono, cantidadHidratoDeCarbonoEnIngrediente, porCada, unidadMedidaHidratoDeCarbonoEnIngrediente):
        self.IdIngrediente = idIngrediente
        self.IdHidratoDeCarbono = idHidratoDeCarbono
        self.CantidadHidratoDeCarbonoEnIngrediente = cantidadHidratoDeCarbonoEnIngrediente
        self.PorCada = porCada
        self.UnidadMedidaHidratoDeCarbonoEnIngrediente = unidadMedidaHidratoDeCarbonoEnIngrediente
    
    def __repr__(self):
        return f"RelationshipFoodCarbohydrate({self.IdIngrediente}, {self.IdHidratoDeCarbono}, {self.CantidadHidratoDeCarbonoEnIngrediente}, {self.PorCada}, {self.UnidadMedidaHidratoDeCarbonoEnIngrediente})"
        
    def __str__(self):
        return self.RelationshipFoodCarbohydrate
    
    def Create(foodID: int,
               carbohydrateID: int,
               carbohydrateInFood: float,
               each: float,
               unitOfMeasure: str):
        carbohydrateToInsert = RelationshipFoodCarbohydrate(foodID,carbohydrateID,carbohydrateInFood,each,unitOfMeasure)
        return carbohydrateToInsert