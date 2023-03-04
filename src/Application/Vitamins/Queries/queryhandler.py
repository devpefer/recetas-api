from src.exceptions import ObjectNotExists
from src.Application.Vitamins.Queries.querymodels import QueryModels
from src.Domain.Vitamins.vitamin import Vitamin
from src.Application.Vitamins.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.vitaminsrepository import VitaminsRepository
from mediatr import Mediator

class QueryHandler():
        
    @Mediator.handler
    def GetVitaminByID(request: QueryModels.GetVitaminByIDQueryModel) -> ReadModels.GetVitaminByIDReadModel:
        vitaminsRepository = VitaminsRepository()
        
        if not vitaminsRepository.Exists(request.VitaminID):
            raise ObjectNotExists(f'Vitamin {request.VitaminID} not exists')
        
        vitaminByID: Vitamin = vitaminsRepository.GetVitaminByID(request.VitaminID)
    
        vitaminByIDReadModel = ReadModels.GetVitaminByIDReadModel(vitaminByID.IdVitamina,
                                                                  vitaminByID.IdCategoriaVitamina,
                                                                  vitaminByID.NombreVitaminaEspanyol,
                                                                  vitaminByID.NombreVitaminaIngles,
                                                                  vitaminByID.NombreVitaminaEuropeo,
                                                                  vitaminByID.DescripcionVitaminaEspanyol,
                                                                  vitaminByID.DescripcionVitaminaIngles)
        
        return vitaminByIDReadModel

    @Mediator.handler
    def GetAllVitamins(request: QueryModels.GetAllVitaminsQueryModel) -> ReadModels.GetAllVitaminsReadModel:
        vitaminsRepository = VitaminsRepository()
        
        allVitamins: list[Vitamin] = vitaminsRepository.GetAllVitamins()

        vitaminList: list[ReadModels.GetVitaminByIDReadModel] = []
        
        for vitamin in allVitamins:
            tmpVitamin = ReadModels.GetVitaminByIDReadModel(vitamin.IdVitamina,
                                                            vitamin.IdCategoriaVitamina,
                                                            vitamin.NombreVitaminaEspanyol,
                                                            vitamin.NombreVitaminaIngles,
                                                            vitamin.NombreVitaminaIngles,
                                                            vitamin.DescripcionVitaminaEspanyol,
                                                            vitamin.DescripcionVitaminaIngles)
            
            vitaminList.append(tmpVitamin)
        
        return vitaminList