from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.Domain.Carbohydrates.carbohydrate import Carbohydrate
from src.Infrastructure.SQLAlchemy.carbohydratesrepository import CarbohydratesRepository
from src.Application.Carbohydrates.Commands.commands import Commands
from mediatr import Mediator

class CommandHandler():
        
    @Mediator.handler
    def InsertCarbohydrate(request: Commands.InsertCarbohydrateCommand):
        carbohydratesRepository = CarbohydratesRepository()
        
        if carbohydratesRepository.ExistsByName(request.NombreEspanyol, request.NombreIngles):
            raise ObjectAlreadyExists(f'Carbohydrate {request.NombreIngles} already exists')
          
        carbohydrate: Carbohydrate = Carbohydrate.Create(request.IdTipoHidratoDeCarbono,
                                                            request.NombreEspanyol,
                                                            request.NombreIngles,
                                                            request.NombreEuropeo,
                                                            request.DescripcionEspanyol,
                                                            request.DescripcionIngles)
        
        carbohydratesRepository.session.add(carbohydrate)
        carbohydratesRepository.session.commit()
       
    @Mediator.handler 
    def DeleteCarbohydrate(request: Commands.DeleteCarbohydrateCommand):
        carbohydratesRepository = CarbohydratesRepository()
        
        if not carbohydratesRepository.Exists(request.IdHidratoDeCarbono):
            raise ObjectNotExists(f'Carbohydrate {request.IdHidratoDeCarbono} not exists')
        
        carbohydrate: Carbohydrate = carbohydratesRepository.GetCarbohydrateByID(request.IdHidratoDeCarbono)
        
        carbohydratesRepository.Delete(carbohydrate)
        
        carbohydratesRepository.session.commit()