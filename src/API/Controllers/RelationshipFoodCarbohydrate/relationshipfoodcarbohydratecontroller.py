from fastapi import APIRouter, HTTPException, Response
from http import HTTPStatus
from src.exceptions import ObjectNotExists, ObjectAlreadyExists
from src.API.Controllers.Shared.requesthandler import RequestHandler
from src.Application.Relationship_Food_Carbohydrates.Commands.commands import Commands
from src.Application.Relationship_Food_Carbohydrates.Queries.querymodels import QueryModels

class RelationshipFoodCarbohydrateController():
    router = APIRouter(
        prefix="/RelationshipFoodCarbohydrate",
        tags=["Relationship Food Carbohydrate"],
    )

    #region GET
    
    @router.get("/GetRelationshipFoodCarbohydrateByID/{foodID}/{carbohydrateID}")
    async def GetRelationshipFoodCarbohydrateByID(foodID: int, carbohydrateID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetRelationshipFoodCarbohydrateByIDQueryModel(foodID,carbohydrateID))
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    @router.get("/GetAllCarbohydratesInFood/{foodID}")
    async def GetAllCarbohydratesInFood(foodID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetAllCarbohydratesInFoodQueryModel(foodID))
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])    
            
    #endregion
    
    #region POST
    
    @router.post("/InsertRelationshipFoodCarbohydrate")
    async def InsertRelationshipFoodCarbohydrate(insertRelationshipFoodCarbohydrateCommand: Commands.InsertRelationshipFoodCarbohydrateCommand):
        requestHandler = RequestHandler()

        try:
            requestHandler.HandleCommand(insertRelationshipFoodCarbohydrateCommand)
            return Response('',HTTPStatus.OK)
        
        except ObjectAlreadyExists as ex:
            raise HTTPException(HTTPStatus.FORBIDDEN, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
    
    #region DELETE
    
    @router.delete("/DeleteRelationshipFoodCarbohydrate/{foodID}/{carbohydrateID}")
    async def DeletetRelationshipFoodCarbohydrate(foodID: int, carbohydrateID: int):
        requestHandler = RequestHandler()

        try:
            requestHandler.HandleCommand(Commands.DeleteRelationshipFoodCarbohydrateCommand(foodID,carbohydrateID))
            return Response('',HTTPStatus.OK)
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
