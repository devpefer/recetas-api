from src.exceptions import ObjectNotExists
from src.Application.Carbohydrates.Queries.querymodels import QueryModels
from src.Domain.Carbohydrates.carbohydrate import Carbohydrate
from src.Application.Carbohydrates.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.carbohydratesrepository import CarbohydratesRepository
from mediatr import Mediator

class CarbohydratesQueryHandler():
      
    @Mediator.handler
    def GetCarbohydrateByID(request: QueryModels.GetCarbohydrateByIDQueryModel) -> ReadModels.GetCarbohydrateByIDReadModel:
        carbohydratesRepository = CarbohydratesRepository()
        
        if not carbohydratesRepository.Exists(request.CarbohydrateID):
            raise ObjectNotExists(f'Carbohydrate {request.CarbohydrateID} not exists')
        
        carbohydrateByID: Carbohydrate = carbohydratesRepository.GetCarbohydrateByID(request.CarbohydrateID)
    
        carbohydrateByIDReadModel = ReadModels.GetCarbohydrateByIDReadModel(carbohydrateByID.IdHidratoDeCarbono,
                                                                            carbohydrateByID.IdTipoHidratoDeCarbono,
                                                                            carbohydrateByID.NombreEspanyol,
                                                                            carbohydrateByID.NombreIngles,
                                                                            carbohydrateByID.NombreEuropeo,
                                                                            carbohydrateByID.DescripcionEspanyol,
                                                                            carbohydrateByID.DescripcionIngles)
        
        return carbohydrateByIDReadModel
    
    @Mediator.handler
    def GetAllCarbohydrates(request: QueryModels.GetAllCarbohydratesQueryModel) -> ReadModels.GetAllCarbohydratesReadModel:
        carbohydratesRepository = CarbohydratesRepository()
        
        allCarbohydrates = carbohydratesRepository.GetAllCarbohydrates()
        
        carbohydrateReadModelList: list[ReadModels.GetCarbohydrateByIDReadModel] = []
        
        for carbohydrate in allCarbohydrates:
            tmpCarbohydrateReadModel = ReadModels.GetCarbohydrateByIDReadModel(carbohydrate.IdHidratoDeCarbono,
                                                                               carbohydrate.IdTipoHidratoDeCarbono,
                                                                               carbohydrate.NombreEspanyol,
                                                                               carbohydrate.NombreIngles,
                                                                               carbohydrate.NombreEuropeo,
                                                                               carbohydrate.DescripcionEspanyol,
                                                                               carbohydrate.DescripcionIngles)
            
            carbohydrateReadModelList.append(tmpCarbohydrateReadModel)
        
        return carbohydrateReadModelList