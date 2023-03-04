from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Response
from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.API.Controllers.Shared.requesthandler import RequestHandler
from src.Application.Carbohydrates.Queries.querymodels import QueryModels
from src.Application.Carbohydrates.Commands.commands import Commands

class CarbohydratesController():
    router = APIRouter(
        prefix="/Carbohydrates",
        tags=["Carbohydrates"],
    )

    #region GET
    
    @router.get("/GetCarbohydrateByID/{carbohydrateID}")
    async def GetCarbohydrateByID(carbohydrateID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetCarbohydrateByIDQueryModel(carbohydrateID))
            
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    @router.get("/GetAllCarbohydrates")
    async def GetAllCarbohydrates():
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetAllCarbohydratesQueryModel())
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region POST
    
    @router.post("/InsertCarbohydrate")
    async def InsertCarbohydrate(insertCarbohydrate: Commands.InsertCarbohydrateCommand):
        requestHandler = RequestHandler()
            
        try:
            requestHandler.HandleCommand(insertCarbohydrate)
            return Response('',HTTPStatus.OK)
        
        except ObjectAlreadyExists as ex:
            raise HTTPException(HTTPStatus.CONFLICT, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region DELETE
    
    @router.delete("/Delete/{carbohydrateID}")
    async def Delete(carbohydrateID):
        commandHandler = RequestHandler()
    
        try:
            commandHandler.HandleCommand(Commands.DeleteCarbohydrateCommand(carbohydrateID))
            return Response('',HTTPStatus.OK)
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
