import os
from src.exceptions import ObjectNotExists
from src.Application.Minerals.Queries.querymodels import QueryModels
from src.Domain.Minerals.mineral import Mineral
from src.Application.Minerals.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.mineralsrepository import MineralsRepository
from mediatr import Mediator

class QueryHandler():
        
    @Mediator.handler
    def GetMineralByID(request: QueryModels.GetMineralByIDQueryModel) -> ReadModels.GetMineralByIDReadModel:
        mineralsRepository = MineralsRepository()
        
        if not mineralsRepository.Exists(request.MineralID):
            raise ObjectNotExists(f'Mineral {request.MineralID} not exists')
        
        mineralByID: Mineral = mineralsRepository.GetMineralByID(request.MineralID)
    
        mineralByIDReadModel = ReadModels.GetMineralByIDReadModel(mineralByID.IdMineral,
                                                                  mineralByID.IdCategoriaMineral,
                                                                  mineralByID.NombreMineralEspanyol,
                                                                  mineralByID.NombreMineralIngles,
                                                                  mineralByID.NombreMineralEuropeo,
                                                                  mineralByID.DescripcionMineralEspanyol,
                                                                  mineralByID.DescripcionMineralIngles)
        
        return mineralByIDReadModel

    @Mediator.handler
    def GetAllMinerals(request: QueryModels.GetAllMineralsQueryModel) -> ReadModels.GetAllMineralsReadModel:
        mineralsRepository = MineralsRepository()
        
        allMinerals: list[Mineral] = mineralsRepository.GetAllMinerals()

        mineralList: list[ReadModels.GetMineralByIDReadModel] = []
        
        for mineral in allMinerals:
            tmpMineral = ReadModels.GetMineralByIDReadModel(mineral.IdMineral,
                                                            mineral.IdCategoriaMineral,
                                                            mineral.NombreMineralEspanyol,
                                                            mineral.NombreMineralIngles,
                                                            mineral.NombreMineralIngles,
                                                            mineral.DescripcionMineralEspanyol,
                                                            mineral.DescripcionMineralIngles)
            
            mineralList.append(tmpMineral)
        
        return mineralList