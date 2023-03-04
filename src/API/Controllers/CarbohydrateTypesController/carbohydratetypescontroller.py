from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Response
from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.API.Controllers.Shared.requesthandler import RequestHandler
from src.Application.CarbohydrateTypes.Queries.querymodels import QueryModels
from src.Application.CarbohydrateTypes.Commands.commands import Commands

class CarbohydrateTypesController():
    router = APIRouter(
        prefix="/CarbohydrateTypes",
        tags=["Carbohydrate Types"],
    )

    #region GET
    
    @router.get("/GetCarbohydrateTypeByID/{carbohydrateTypeID}")
    async def GetCarbohydrateTypeByID(carbohydrateTypeID: int):
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetCarbohydrateTypeByIDQueryModel(carbohydrateTypeID))
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    @router.get("/GetAllCarbohydrateTypes")
    async def GetAllCarbohydrateTypes():
        requestHandler = RequestHandler()
        
        try:
            return requestHandler.HandleQuery(QueryModels.GetAllCarbohydrateTypesQueryModel())
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region POST
    @router.post("/InsertCarbohydrateType")
    async def InsertCarbohydrate(carbohydrateType: Commands.InsertCarbohydrateTypeCommand):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(carbohydrateType)
            return Response('',HTTPStatus.OK)
        
        except ObjectAlreadyExists as ex:
            raise HTTPException(HTTPStatus.CONFLICT, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion

    #region DELETE
    
    @router.delete("/Delete/{carbohydrateTypeID}")
    async def Delete(carbohydrateTypeID):
        requestHandler = RequestHandler()
    
        try:
            requestHandler.HandleCommand(Commands.DeleteCarbohydrateTypeCommand(carbohydrateTypeID))
            return Response('',HTTPStatus.OK)
        
        except ObjectNotExists as ex:
            raise HTTPException(HTTPStatus.NOT_FOUND, detail=ex.args[0])
        
        except Exception as ex:
            raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail=ex.args[0])
        
    #endregion
