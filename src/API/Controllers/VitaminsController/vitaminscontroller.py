from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Response
from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.API.Controllers.Shared.requesthandler import RequestHandler
from src.Application.Vitamins.Queries.querymodels import QueryModels
from src.Application.Vitamins.Commands.commands import Commands

class VitaminsController():
    
    router = APIRouter(
        prefix="/Vitamins",
        tags=["Vitamins"],
    )

    #region GET
    
    @router.get("/GetVitaminByID/{mineralID}")
    async def GetVitaminByID(vitaminID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetVitaminByIDQueryModel(vitaminID))
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    @router.get("/GetAllVitamins")
    async def GetAllVitamins():
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetAllVitaminsQueryModel())
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region POST
    
    @router.post("/InsertVitamin")
    async def InsertVitamin(insertVitaminCommand: Commands.InsertVitaminCommand):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(insertVitaminCommand)
            return Response('',HTTPStatus.OK)
        
        except ObjectAlreadyExists as ex:
            raise HTTPException(HTTPStatus.CONFLICT, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region DELETE
    
    @router.delete("/Delete/{vitaminID}")
    async def Delete(vitaminID):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(Commands.DeleteVitaminCommand(vitaminID))
            return Response('',HTTPStatus.OK)
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
