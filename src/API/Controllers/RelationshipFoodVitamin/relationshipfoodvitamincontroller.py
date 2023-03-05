from fastapi import APIRouter, HTTPException, Response
from http import HTTPStatus
from src.exceptions import ObjectNotExists, ObjectAlreadyExists
from src.API.Controllers.Shared.requesthandler import RequestHandler
from src.Application.Relationship_Food_Vitamins.Commands.commands import Commands
from src.Application.Relationship_Food_Vitamins.Queries.querymodels import QueryModels

class RelationshipFoodVitaminController():
    router = APIRouter(
        prefix="/RelationshipFoodVitamins",
        tags=["Relationship Food Vitamins"],
    )

    #region GET
    
    @router.get("/GetRelationshipFoodVitaminByID/{foodID}/{vitaminID}")
    async def GetRelationshipFoodVitaminByID(foodID: int, vitaminID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetRelationshipFoodVitaminByIDQueryModel(foodID,vitaminID))
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    @router.get("/GetAllVitaminsInFood/{foodID}")
    async def GetAllVitaminsInFood(foodID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetAllVitaminsInFoodQueryModel(foodID))
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])    
            
    #endregion
    
    #region POST
    
    @router.post("/InsertRelationshipFoodVitamin")
    async def InsertRelationshipFoodVitamin(insertRelationshipFoodVitaminCommand: Commands.InsertRelationshipFoodVitaminCommand):
        requestHandler = RequestHandler()

        try:
            requestHandler.HandleCommand(insertRelationshipFoodVitaminCommand)
            return Response('',HTTPStatus.OK)
        
        except ObjectAlreadyExists as ex:
            raise HTTPException(HTTPStatus.CONFLICT, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
    
    #region DELETE
    
    @router.delete("/DeleteRelationshipFoodVitamin/{foodID}/{vitaminID}")
    async def DeletetRelationshipFoodVitamin(foodID: int, vitaminID: int):
        requestHandler = RequestHandler()

        try:
            requestHandler.HandleCommand(Commands.DeleteRelationshipFoodVitaminCommand(foodID,vitaminID))
            return Response('',HTTPStatus.OK)
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
