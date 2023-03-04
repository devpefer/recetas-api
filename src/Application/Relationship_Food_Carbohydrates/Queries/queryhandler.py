import os
from src.exceptions import ObjectNotExists
from src.Application.Relationship_Food_Carbohydrates.Queries.querymodels import QueryModels
from src.Domain.Relationship_Food_Carbohydrates.relationship_food_carbohydrate import RelationshipFoodCarbohydrate
from src.Application.Relationship_Food_Carbohydrates.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.relationshipfoodcarbohydraterepository import RelationshipFoodCarbohydrateRepository
from mediatr import Mediator

class QueryHandler():
        
    @Mediator.handler
    def GetRelationshipFoodCarbohydrateByID(request: QueryModels.GetRelationshipFoodCarbohydrateByIDQueryModel) -> ReadModels.GetRelationshipFoodCarbohydrateByIDReadModel:
        relationshipFoodCarbohydrateRepository = RelationshipFoodCarbohydrateRepository()
        
        if not relationshipFoodCarbohydrateRepository.Exists(request.FoodID,request.CarbohydrateID):
            raise ObjectNotExists(f'RelationshipFoodCarbohydrate {request.FoodID} {request.CarbohydrateID} not exists')
        
        relationshipFoodCarbohydrateByID: RelationshipFoodCarbohydrate = relationshipFoodCarbohydrateRepository.GetRelationshipFoodCarbohydrateByID(request.FoodID, request.CarbohydrateID)
    
        relationshipFoodCarbohydrateByIDReadModel = ReadModels.GetRelationshipFoodCarbohydrateByIDReadModel(relationshipFoodCarbohydrateByID.IdIngrediente,
                                                                                                            relationshipFoodCarbohydrateByID.IdHidratoDeCarbono,
                                                                                                            relationshipFoodCarbohydrateByID.CantidadHidratoDeCarbonoEnIngrediente,
                                                                                                            relationshipFoodCarbohydrateByID.PorCada,
                                                                                                            relationshipFoodCarbohydrateByID.UnidadMedidaHidratoDeCarbonoEnIngrediente)
        
        
        return relationshipFoodCarbohydrateByIDReadModel
    
    @Mediator.handler
    def GetAllCarbohydratesInFood(request: QueryModels.GetAllCarbohydratesInFoodQueryModel) -> ReadModels.GetAllCarbohydratesInFoodReadModel:
        relationshipFoodCarbohydrateRepository = RelationshipFoodCarbohydrateRepository()
        
        carbohydratesInFood: list[RelationshipFoodCarbohydrate] = relationshipFoodCarbohydrateRepository.GetAllCarbohydratesInFood(request.FoodID)
        
        carbohydratesInFoodList: list[ReadModels.GetRelationshipFoodCarbohydrateByIDReadModel] = []
        
        for carbohydrate in carbohydratesInFood:
            tmpCarbohydrate = ReadModels.GetRelationshipFoodCarbohydrateByIDReadModel(carbohydrate.IdIngrediente,carbohydrate.IdHidratoDeCarbono,carbohydrate.CantidadHidratoDeCarbonoEnIngrediente,carbohydrate.PorCada,carbohydrate.UnidadMedidaHidratoDeCarbonoEnIngrediente)
            carbohydratesInFood.append(tmpCarbohydrate)
        
        return carbohydratesInFoodList