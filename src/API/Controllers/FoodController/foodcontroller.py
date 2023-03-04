from fastapi import APIRouter
from src.Application.Food.Queries.querymodels import QueryModels
from src.Application.Food.Commands.commands import FoodCommands
from src.Application.Food.Commands.commandhandler import CommandHandler
from src.Application.Food.Queries.queryhandler import FoodQueryHandler
import os

class FoodController():
    router = APIRouter(
        prefix="/Food",
        tags=["Food"],
    )

    #region GET
    @router.get("/GetFoodByID/{foodID}")
    async def GetFoodByID(foodID: int):
        queryHandler = FoodQueryHandler()
        getFoodByIDQueryModel = QueryModels.GetFoodByIDQueryModel
        getFoodByIDQueryModel.FoodID = foodID
        return queryHandler.GetFoodByID(getFoodByIDQueryModel)
    
    @router.get("/DownloadAllFoodsToJSON")
    async def DownloadAllFoodsToJSON():
        queryHandler = FoodQueryHandler()
        return queryHandler.DownloadAllFoodsToJSON()
    
    @router.get("/GetAllFood")
    async def GetAllFood():
        queryHandler = FoodQueryHandler()
        listFiles = os.listdir('/Users/devpefer/BEDCARESPONSES')
        return queryHandler.GetAllFood(listFiles)
    
    @router.get("/CategorizarAlimentos")
    async def CategorizarAlimentos():
        queryHandler = FoodQueryHandler()
        return queryHandler.CategorizarAlimentos()
    #endregion

'''
    #region POST
    @router.post("/Crear")
    async def Crear(acabado: commands.InsertarAcabadoCommand):
        commandHandler = CommandHandler()
        return commandHandler.Crear(acabado)

    @router.post("/ModificarDescripcion")
    async def ModificarDescripcion(modificarAcabado: commands.ModificarAcabadoDescripcionCommand):
        commandHandler = CommandHandler()
        return commandHandler.ModificarDescripcion(modificarAcabado)

    @router.post("/ModificarPrecio")
    async def ModificarPrecio(modificarAcabado: commands.ModificarAcabadoPrecioCommand):
        commandHandler = CommandHandler()
        return commandHandler.ModificarPrecio(modificarAcabado)
    #endregion

    #region DELETE
    @router.delete("/Eliminar/{acabado}")
    async def Eliminar(acabado):
        commandHandler = CommandHandler()
        return commandHandler.Eliminar(acabado)
    #endregion
'''