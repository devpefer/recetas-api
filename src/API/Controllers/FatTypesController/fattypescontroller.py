from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Response
from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.API.Controllers.Shared.requesthandler import RequestHandler
from src.Application.FatTypes.Queries.querymodels import QueryModels
from src.Application.FatTypes.Commands.commands import Commands

class FatTypesController():
    router = APIRouter(
        prefix="/FatTypes",
        tags=["Fat Types"],
    )

    #region GET
    
    @router.get("/GetFatTypeByID/{fatTypeID}")
    async def GetFatTypeByID(fatTypeID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetFatTypeByIDQueryModel(fatTypeID))
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(500, detail=ex.args[0])
        
    @router.get("/GetAllFatTypes")
    async def GetFatTypeByID():
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetAllFatTypesQueryModel())
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(500, detail=ex.args[0])
        
    #endregion

    #region POST
    
    @router.post("/InsertFatType")
    async def InsertFatType(insertFatTypeCommand: Commands.InsertFatTypeCommand):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(insertFatTypeCommand)
            return Response('',HTTPStatus.OK)
        
        except ObjectAlreadyExists as ex:
            raise HTTPException(HTTPStatus.FORBIDDEN, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region DELETE
    
    @router.delete("/Delete/{fatTypeID}")
    async def Delete(fatTypeID):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(Commands.DeleteFatTypeCommand(fatTypeID))
            return Response('',HTTPStatus.OK)
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
