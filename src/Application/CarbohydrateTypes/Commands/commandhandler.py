from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.Domain.CarbohydrateTypes.carbohydratetypes import CarbohydrateType
from src.Infrastructure.SQLAlchemy.carbohydratetypesrepository import CarbohydrateTypesRepository
from src.Application.CarbohydrateTypes.Commands.commands import Commands
from mediatr import Mediator

class CommandHandler():

    @Mediator.handler
    def InsertCarbohydrateType(request: Commands.InsertCarbohydrateTypeCommand):
        carbohydrateTypesRepository = CarbohydrateTypesRepository()
        
        if carbohydrateTypesRepository.ExistsByName(request.Tipo):
            raise ObjectAlreadyExists(f'CarbohydrateType {request.Tipo} already exists')
          
        carbohydrateType: CarbohydrateType = CarbohydrateType.Create(request.Tipo, request.Descripcion)
        
        carbohydrateTypesRepository.session.add(carbohydrateType)
        carbohydrateTypesRepository.session.commit()
    
    @Mediator.handler  
    def DeleteCarbohydrateType(request: Commands.DeleteCarbohydrateTypeCommand):
        carbohydrateTypesRepository = CarbohydrateTypesRepository()
        
        if not carbohydrateTypesRepository.Exists(request.CarbohydrateTypeID):
            raise ObjectNotExists(f'CarbohydrateType {request.CarbohydrateTypeID} not exists')
        
        carbohydrateType: CarbohydrateType = carbohydrateTypesRepository.GetCarbohydrateTypeByID(request.CarbohydrateTypeID)
        
        carbohydrateTypesRepository.Delete(carbohydrateType)
        
        carbohydrateTypesRepository.session.commit()