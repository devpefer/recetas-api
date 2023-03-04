from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Response
from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.API.Controllers.Shared.requesthandler import RequestHandler
from src.Application.FatSubtypes.Queries.querymodels import QueryModels
from src.Application.FatSubtypes.Commands.commands import Commands

class FatSubtypesController():
    router = APIRouter(
        prefix="/FatSubtypes",
        tags=["Fat Subtypes"],
    )

    #region GET
    
    @router.get("/GetFatSubtypeByID/{fatSubtypeID}")
    async def GetFatSubtypeByID(fatSubtypeID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetFatSubtypeByIDQueryModel(fatSubtypeID))
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    @router.get("/GetAllFatSubtypes")
    async def GetAllFatSubtypes():
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetAllFatSubtypesQueryModel())
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region POST
    
    @router.post("/InsertFatSubtype")
    async def InsertFatSubtype(insertFatSubtypeCommand: Commands.InsertFatSubtypeCommand):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleQuery(insertFatSubtypeCommand)
            return Response('',HTTPStatus.OK)
        
        except ObjectAlreadyExists as ex:
            raise HTTPException(HTTPStatus.FORBIDDEN, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region DELETE
    
    @router.delete("/Delete/{fatSubtypeID}")
    async def Delete(fatSubtypeID):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(Commands.DeleteFatSubtypeCommand(fatSubtypeID))
            return Response('',HTTPStatus.OK)
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
