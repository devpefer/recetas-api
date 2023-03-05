from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Domain.Relationship_Food_Carbohydrates.relationship_food_carbohydrate import RelationshipFoodCarbohydrate
from src.Infrastructure.SQLAlchemy import secrets

class RelationshipFoodCarbohydrateRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
    
    def GetRelationshipFoodCarbohydrateByID(self,foodID: int, carbohydrateID: int) -> RelationshipFoodCarbohydrate:
        query = self.session.query(RelationshipFoodCarbohydrate).get((foodID,carbohydrateID,))
        return query
        
    def GetAllCarbohydratesInFood(self,idIngrediente) -> list[RelationshipFoodCarbohydrate]:
        query = self.session.query(RelationshipFoodCarbohydrate).filter(RelationshipFoodCarbohydrate.IdIngrediente == idIngrediente).all()
        return query
        
    def Exists(self,relationshipFoodCarbohydrateIDFood: int, relationshipFoodCarbohydrateIDCarbohydrate: int) -> bool:
        query = self.session.query(exists().where(RelationshipFoodCarbohydrate.IdIngrediente == relationshipFoodCarbohydrateIDFood, RelationshipFoodCarbohydrate.IdHidratoDeCarbono == relationshipFoodCarbohydrateIDCarbohydrate)).scalar()
        return query
        
    def Delete(self,relationshipFoodCarbohydrate: RelationshipFoodCarbohydrate):
        self.session.delete(relationshipFoodCarbohydrate)