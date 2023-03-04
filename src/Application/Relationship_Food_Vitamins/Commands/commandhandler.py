from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.Domain.Relationship_Food_Vitamins.relationship_food_vitamin import RelationshipFoodVitamin
from src.Infrastructure.SQLAlchemy.relationshipfoodvitaminrepository import RelationshipFoodVitaminRepository
from src.Application.Relationship_Food_Vitamins.Commands.commands import Commands
from mediatr import Mediator

class CommandHandler():
        
    @Mediator.handler
    def InsertRelationshipFoodVitamin(request: Commands.InsertRelationshipFoodVitaminCommand):
        relationshipFoodVitaminRepository = RelationshipFoodVitaminRepository()
        
        if relationshipFoodVitaminRepository.Exists(request.FoodID,request.VitaminID):
            raise ObjectAlreadyExists(f'RelationshipFoodVitamin {request.FoodID} {request.VitaminID} already exists')
        
        relationshipFoodVitamin: RelationshipFoodVitamin = RelationshipFoodVitamin.Create(request)
        
        relationshipFoodVitaminRepository.session.add(relationshipFoodVitamin)
        relationshipFoodVitaminRepository.session.commit()
        
    @Mediator.handler
    def DeleteRelationshipFoodVitamin(request: Commands.DeleteRelationshipFoodVitaminCommand):
        relationshipFoodVitaminRepository = RelationshipFoodVitaminRepository()
        
        if not relationshipFoodVitaminRepository.Exists(request.FoodID, request.VitaminID):
            raise ObjectNotExists(f'RelationshipFoodVitamin {request.FoodID} {request.VitaminID} not exists')
        
        relationshipFoodVitamin: RelationshipFoodVitamin = relationshipFoodVitaminRepository.GetRelationshipFoodVitaminByID(request.FoodID,request.CarbohydrateID)
        
        relationshipFoodVitaminRepository.Delete(relationshipFoodVitamin)
        relationshipFoodVitaminRepository.session.commit()