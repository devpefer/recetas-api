import os
from src.exceptions import ObjectNotExists
from src.Application.CarbohydrateTypes.Queries.querymodels import QueryModels
from src.Domain.CarbohydrateTypes.carbohydratetypes import CarbohydrateType
from src.Application.CarbohydrateTypes.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.carbohydratetypesrepository import CarbohydrateTypesRepository
from mediatr import Mediator

class QueryHandler():
        
    @Mediator.handler
    def GetCarbohydrateTypeByID(request: QueryModels.GetCarbohydrateTypeByIDQueryModel) -> ReadModels.GetCarbohydrateTypeByIDReadModel:
        carbohydrateTypesRepository = CarbohydrateTypesRepository()
        
        if not carbohydrateTypesRepository.Exists(request.CarbohydrateTypeID):
            raise ObjectNotExists(f'CarbohydrateType {request.CarbohydrateTypeID} not exists')
        
        carbohydrateTypeByID: CarbohydrateType = carbohydrateTypesRepository.GetCarbohydrateTypeByID(request.CarbohydrateTypeID)
    
        carbohydrateTypeByIDReadModel = ReadModels.GetCarbohydrateTypeByIDReadModel(carbohydrateTypeByID.IdTipoHidratoDeCarbono,
                                                                                    carbohydrateTypeByID.Tipo,
                                                                                    carbohydrateTypeByID.Descripcion)
        
        return carbohydrateTypeByIDReadModel

    @Mediator.handler
    def GetAllCarbohydrateTypes(request: QueryModels.GetAllCarbohydrateTypesQueryModel) -> ReadModels.GetAllCarbohydrateTypesReadModel:
        carbohydrateTypesRepository = CarbohydrateTypesRepository()
        
        allCarbohydrateTypes: list[CarbohydrateType] = carbohydrateTypesRepository.GetAllCarbohydrateTypes()
    
        carbohydrateTypesReadModelList: list[ReadModels.GetCarbohydrateTypeByIDReadModel] = []
        
        for carbohydrateType in allCarbohydrateTypes:
            tmpCarbohydrateType = ReadModels.GetCarbohydrateTypeByIDReadModel(carbohydrateType.IdTipoHidratoDeCarbono,carbohydrateType.Tipo,carbohydrateType.Descripcion)
            carbohydrateTypesReadModelList.append(tmpCarbohydrateType)
        
        return carbohydrateTypesReadModelList