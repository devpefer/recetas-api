from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Response
from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.API.Controllers.Shared.requesthandler import RequestHandler
from src.Application.Minerals.Queries.querymodels import QueryModels
from src.Application.Minerals.Commands.commands import Commands

class MineralsController():
    
    router = APIRouter(
        prefix="/Minerals",
        tags=["Minerals"],
    )

    #region GET
    
    @router.get("/GetMineralByID/{mineralID}")
    async def GetMineralByID(mineralID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetMineralByIDQueryModel(mineralID))
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    @router.get("/GetAllMinerals")
    async def GetAllMinerals():
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetAllMineralsQueryModel())
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region POST
    
    @router.post("/InsertMineral")
    async def InsertMineral(insertMineralCommand: Commands.InsertMineralCommand):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(insertMineralCommand)
            return Response('',HTTPStatus.OK)
        
        except ObjectAlreadyExists as ex:
            raise HTTPException(HTTPStatus.CONFLICT, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region DELETE
    
    @router.delete("/Delete/{mineralID}")
    async def Delete(mineralID):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(Commands.DeleteMineralCommand(mineralID))
            return Response('',HTTPStatus.OK)
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
