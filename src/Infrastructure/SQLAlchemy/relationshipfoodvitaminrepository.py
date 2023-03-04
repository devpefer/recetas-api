from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Domain.Relationship_Food_Vitamins.relationship_food_vitamin import RelationshipFoodVitamin
from src.Infrastructure.SQLAlchemy import secrets

class RelationshipFoodVitaminRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
    
    def GetRelationshipFoodVitaminByID(self,foodID: int, carbohydrateID: int) -> RelationshipFoodVitamin:
        query = self.session.query(RelationshipFoodVitamin).get((foodID,carbohydrateID,))
        return query
        
    def GetAllVitaminsInFood(self,idIngrediente) -> list[RelationshipFoodVitamin]:
        query = self.session.query(RelationshipFoodVitamin).filter(RelationshipFoodVitamin.IdIngrediente == idIngrediente).all()
        return query
        
    def Exists(self,relationshipFoodVitaminIDFood: int, relationshipFoodVitaminIDCarbohydrate: int) -> bool:
        query = self.session.query(exists().where(RelationshipFoodVitamin.IdIngrediente == relationshipFoodVitaminIDFood, RelationshipFoodVitamin.IdVitamina == relationshipFoodVitaminIDCarbohydrate)).scalar()
        return query
        
    def Delete(self,relationshipFoodVitamin: RelationshipFoodVitamin):
        self.session.delete(relationshipFoodVitamin)