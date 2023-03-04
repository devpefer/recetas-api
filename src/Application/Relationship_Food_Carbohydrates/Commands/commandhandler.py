from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.Domain.Relationship_Food_Carbohydrates.relationship_food_carbohydrate import RelationshipFoodCarbohydrate
from src.Infrastructure.SQLAlchemy.relationshipfoodcarbohydraterepository import RelationshipFoodCarbohydrateRepository
from src.Application.Relationship_Food_Carbohydrates.Commands.commands import Commands
from mediatr import Mediator

class CommandHandler():
        
    @Mediator.handler
    def InsertRelationshipFoodCarbohydrate(request: Commands.InsertRelationshipFoodCarbohydrateCommand):
        relationshipFoodCarbohydrateRepository = RelationshipFoodCarbohydrateRepository()
        
        if relationshipFoodCarbohydrateRepository.Exists(request.FoodID,request.CarbohydrateID):
            raise ObjectAlreadyExists(f'RelationshipFoodCarbohydrate {request.FoodID} {request.CarbohydrateID} already exists')
        
        relationshipFoodCarbohydrate: RelationshipFoodCarbohydrate = RelationshipFoodCarbohydrate.Create(request)
        
        relationshipFoodCarbohydrateRepository.session.add(relationshipFoodCarbohydrate)
        relationshipFoodCarbohydrateRepository.session.commit()
        
    @Mediator.handler
    def DeleteRelationshipFoodCarbohydrate(request: Commands.DeleteRelationshipFoodCarbohydrateCommand):
        relationshipFoodCarbohydrateRepository = RelationshipFoodCarbohydrateRepository()
        
        if not relationshipFoodCarbohydrateRepository.Exists(request.FoodID, request.CarbohydrateID):
            raise ObjectNotExists(f'RelationshipFoodCarbohydrate {request.FoodID} {request.CarbohydrateID} not exists')
        
        relationshipFoodCarbohydrate: RelationshipFoodCarbohydrate = relationshipFoodCarbohydrateRepository.GetRelationshipFoodCarbohydrateByID(request.FoodID,request.CarbohydrateID)
        
        relationshipFoodCarbohydrateRepository.Delete(relationshipFoodCarbohydrate)
        relationshipFoodCarbohydrateRepository.session.commit()