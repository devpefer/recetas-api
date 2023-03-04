import os
from src.exceptions import ObjectNotExists
from src.Application.Fats.Queries.querymodels import QueryModels
from src.Domain.Fats.fat import Fat
from src.Application.Fats.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.fatsrepository import FatsRepository
from mediatr import Mediator

class QueryHandler():
        
    @Mediator.handler
    def GetFatByID(request: QueryModels.GetFatByIDQueryModel) -> ReadModels.GetFatByIDReadModel:
        fatsRepository = FatsRepository()
        
        if not fatsRepository.Exists(request.FatID):
            raise ObjectNotExists(f'Fat {request.FatID} not exists')
        
        fatByID = fatsRepository.GetFatByID(request.FatID)
    
        fatByIDReadModel = ReadModels.GetFatByIDReadModel(fatByID.IdGrasa,
                                                          fatByID.IdTipoGrasa,
                                                          fatByID.NombreEspanyol,
                                                          fatByID.NombreIngles,
                                                          fatByID.NombreEuropeo,
                                                          fatByID.DescripcionEspanyol,
                                                          fatByID.DescripcionIngles)
    
        return fatByIDReadModel
    
    @Mediator.handler
    def GetAllFats(request: QueryModels.GetAllFatsQueryModel) -> list[ReadModels.GetFatByIDReadModel]:
        fatsRepository = FatsRepository()
        
        allFats: list[Fat] = fatsRepository.GetAllFats()
        
        fatList: list[ReadModels.GetFatByIDReadModel] = []
    
        for fat in allFats:
            tmpFatReadModel = ReadModels.GetFatByIDReadModel(fat.IdGrasa,fat.IdTipoGrasa,fat.NombreEspanyol,fat.NombreIngles,fat.NombreEuropeo,fat.DescripcionEspanyol,fat.DescripcionIngles)
            fatList.append(tmpFatReadModel)
        
        return fatList