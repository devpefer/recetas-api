from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, Integer

class Food(Base):
    __tablename__ = 'INGREDIENTES'
    IDIngrediente = Column(Integer, primary_key=True)
    IDIngredienteTipo = Column(Integer)
    NombreIngrediente = Column(String)
    DescripcionIngrediente = Column(String)
    
    def __init__(self,idIngrediente, idIngredienteTipo, nombreIngrediente, descripcionIngrediente):
        self.IDIngrediente = idIngrediente
        self.IDIngredienteTipo = idIngredienteTipo
        self.NombreIngrediente = nombreIngrediente
        self.DescripcionIngrediente = descripcionIngrediente
    
    def __repr__(self):
        return f"Food({self.IDIngrediente}, {self.IDIngredienteTipo}, {self.NombreIngrediente}, {self.DescripcionIngrediente})"
        
    def __str__(self):
        return self.Food
    
    def Create(foodTypeID: int,
               foodName: str,
               foodDescription: str):
        foodToInsert = Food(None,foodTypeID,foodName,foodDescription)
        return foodToInsert
    
    def ModifyName(self, newName: str):
        self.NombreIngrediente = newName
        
    def ModifyDescription(self, newDescription: str):
        self.DescripcionIngrediente = newDescription