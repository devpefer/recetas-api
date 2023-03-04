from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Response
from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.API.Controllers.Shared.requesthandler import RequestHandler
from src.Application.Fats.Queries.querymodels import QueryModels
from src.Application.Fats.Commands.commands import Commands
import json

class FatsController():
    router = APIRouter(
        prefix="/Fats",
        tags=["Fats"],
    )

    #region GET
    @router.get("/GetFatByID/{fatID}")
    async def GetFatByID(fatID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetFatByIDQueryModel(fatID))
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(500, detail=ex.args[0])
        
    @router.get("/GetAllFats/{fatID}")
    async def GetAllFats():
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetAllFatsQueryModel())
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(500, detail=ex.args[0])
        
    #endregion

    #region POST
    
    @router.post("/InsertFat")
    async def InsertFat(insertFatCommand: Commands.InsertFatCommand):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(insertFatCommand)
            return Response('',HTTPStatus.OK)
        
        except ObjectAlreadyExists as ex:
            raise HTTPException(HTTPStatus.FORBIDDEN, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region DELETE
    @router.delete("/Delete/{fatID}")
    async def Delete(fatID):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(Commands.DeleteFatCommand(fatID))
            return Response('',HTTPStatus.OK)
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
