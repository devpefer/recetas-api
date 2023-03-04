from src.exceptions import ObjectNotExists
from src.Application.Relationship_Food_Vitamins.Queries.querymodels import QueryModels
from src.Domain.Relationship_Food_Vitamins.relationship_food_vitamin import RelationshipFoodVitamin
from src.Application.Relationship_Food_Vitamins.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.relationshipfoodvitaminrepository import RelationshipFoodVitaminRepository
from mediatr import Mediator

class QueryHandler():
        
    @Mediator.handler
    def GetRelationshipFoodVitaminByID(request: QueryModels.GetRelationshipFoodVitaminByIDQueryModel) -> ReadModels.GetRelationshipFoodVitaminByIDReadModel:
        relationshipFoodVitaminRepository = RelationshipFoodVitaminRepository()
        
        if not relationshipFoodVitaminRepository.Exists(request.FoodID,request.VitaminID):
            raise ObjectNotExists(f'RelationshipFoodVitamin {request.FoodID} {request.VitaminID} not exists')
        
        relationshipFoodVitaminByID: RelationshipFoodVitamin = relationshipFoodVitaminRepository.GetRelationshipFoodVitaminByID(
            request.FoodID,
            request.VitaminID)
    
        relationshipFoodVitaminByIDReadModel = ReadModels.GetRelationshipFoodVitaminByIDReadModel(
            relationshipFoodVitaminByID.IdIngrediente,
            relationshipFoodVitaminByID.IdHidratoDeCarbono,
            float(relationshipFoodVitaminByID.CantidadHidratoDeCarbonoEnIngrediente),
            relationshipFoodVitaminByID.PorCada,
            relationshipFoodVitaminByID.UnidadMedidaHidratoDeCarbonoEnIngrediente)
        
        return relationshipFoodVitaminByIDReadModel
    
    @Mediator.handler
    def GetAllVitaminsInFood(request: QueryModels.GetAllVitaminsInFoodQueryModel) -> ReadModels.GetAllVitaminsInFoodReadModel:
        relationshipFoodVitaminRepository = RelationshipFoodVitaminRepository()
        
        carbohydratesInFood: list[RelationshipFoodVitamin] = relationshipFoodVitaminRepository.GetAllVitaminsInFood(
            request.FoodID)
        
        carbohydratesInFoodList: list[ReadModels.GetRelationshipFoodVitaminByIDReadModel] = []
        
        for carbohydrate in carbohydratesInFood:
            tmpCarbohydrate = ReadModels.GetRelationshipFoodVitaminByIDReadModel(
                carbohydrate.IdIngrediente,
                carbohydrate.IdVitamina,
                carbohydrate.CantidadVitaminaEnIngrediente,
                carbohydrate.PorCada,
                carbohydrate.UnidadMedidaVitaminaEnIngrediente)
            
            carbohydratesInFoodList.append(tmpCarbohydrate)
        
        return carbohydratesInFoodList