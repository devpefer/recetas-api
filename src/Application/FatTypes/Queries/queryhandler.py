import os
from src.exceptions import ObjectNotExists
from src.Application.FatTypes.Queries.querymodels import QueryModels
from src.Domain.FatTypes.fattype import FatType
from src.Application.FatTypes.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.fattypesrepository import FatTypesRepository
from mediatr import Mediator

class QueryHandler():
        
    @Mediator.handler
    def GetFatTypeByID(request: QueryModels.GetFatTypeByIDQueryModel) -> ReadModels.GetFatTypeByIDReadModel:
        fatTypesRepository = FatTypesRepository()
        
        if not fatTypesRepository.ExistsByID(request.FatTypeID):
            raise ObjectNotExists(f'FatType {request.FatTypeID} not exists')
        
        fatSubtypeByID: FatType = fatTypesRepository.GetFatTypeByID(request.FatTypeID)
    
        fatSubtypeByIDReadModel = ReadModels.GetFatTypeByIDReadModel(fatSubtypeByID.IdTipoGrasa,
                                                                     fatSubtypeByID.Tipo,
                                                                     fatSubtypeByID.Descripcion)
        
        return fatSubtypeByIDReadModel
    
    @Mediator.handler
    def GetAllFatTypes(request: QueryModels.GetAllFatTypesQueryModel) -> ReadModels.GetFatTypeByIDReadModel:
        fatTypesRepository = FatTypesRepository()
        
        getAllFatSubtypesList: list[FatType] = fatTypesRepository.GetAllFatTypes()
        
        fatSubtypeList: list[ReadModels.GetFatTypeByIDReadModel] = []
    
        for fatSutype in getAllFatSubtypesList:
            fatSubtypeByIDReadModel = ReadModels.GetFatTypeByIDReadModel(fatSutype.IdTipoGrasa,
                                                                         fatSutype.Tipo,
                                                                         fatSutype.Descripcion)
            
            fatSubtypeList.append(fatSubtypeByIDReadModel)
        
        return fatSubtypeList
    