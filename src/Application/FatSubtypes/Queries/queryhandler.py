import os
from src.exceptions import ObjectNotExists
from src.Application.FatSubtypes.Queries.querymodels import QueryModels
from src.Domain.FatSubtypes.fatsubtype import FatSubtype
from src.Application.FatSubtypes.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.fatsubtypesrepository import FatSubtypesRepository
from mediatr import Mediator

class QueryHandler():
        
    @Mediator.handler
    def GetFatSubtypeByID(request: QueryModels.GetFatSubtypeByIDQueryModel) -> ReadModels.GetFatSubtypeByIDReadModel:
        fatSubtypesRepository = FatSubtypesRepository()
        
        if not fatSubtypesRepository.ExistsByID(request.FatSubtypeID):
            raise ObjectNotExists(f'FatSubtype {request.FatSubtypeID} not exists')
        
        fatSubtypeByID = fatSubtypesRepository.GetFatSubtypeByID(request.FatSubtypeID)
    
        fatSubtypeByIDReadModel = ReadModels.GetFatSubtypeByIDReadModel(fatSubtypeByID.IdSubtipoGrasa,
                                                                        fatSubtypeByID.IdTipoGrasa,
                                                                        fatSubtypeByID.Subtipo,
                                                                        fatSubtypeByID.Descripcion)
        
        return fatSubtypeByIDReadModel
    
    @Mediator.handler
    def GetAllFatSubtypes(request: QueryModels.GetAllFatSubtypesQueryModel) -> ReadModels.GetFatSubtypeByIDReadModel:
        fatSubtypesRepository = FatSubtypesRepository()
        
        getAllfatSubtypes: list[FatSubtype] = fatSubtypesRepository.GetAllFatSubtypes()
        
        fatSubtypesList: list[ReadModels.GetFatSubtypeByIDReadModel] = []
    
        for fatSubtype in getAllfatSubtypes:
            tmpFatSubtypeByIDReadModel = ReadModels.GetFatSubtypeByIDReadModel(fatSubtype.IdSubtipoGrasa,
                                                                               fatSubtype.IdTipoGrasa,
                                                                               fatSubtype.Subtipo,
                                                                               fatSubtype.Descripcion)
            
            fatSubtypesList.append(tmpFatSubtypeByIDReadModel)
        
        return fatSubtypesList
    