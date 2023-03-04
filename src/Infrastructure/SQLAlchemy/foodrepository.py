from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Food.Commands.commands import FoodCommands
from src.Domain.Food.food import Food
from src.Infrastructure.SQLAlchemy import secrets

class FoodRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
    
    def GetFoodByID(self,foodID: int) -> Food:
        query = self.session.query(Food).get((foodID,))
        return query
        
    def GetAllFood(self) -> list[Food]:
        query = self.session.query(Food).all()
        return query
    
    def GetLastFoodID(self) -> Food:
        query = self.session.query(Food).order_by(Food.IDIngrediente.desc()).first()
        return query
        
    def Exists(self,foodID: int) -> bool:
        query = self.session.query(exists().where(Food.IDIngrediente == foodID)).scalar()
        return query
    
    def ExistsByName(self,foodName: str) -> bool:
        query = self.session.query(exists().where(Food.NombreIngrediente == foodName)).scalar()
        return query
        
    def Delete(self,food: Food):
        self.session.delete(food)