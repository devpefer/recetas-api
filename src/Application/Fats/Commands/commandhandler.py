from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.Domain.Fats.fat import Fat
from src.Infrastructure.SQLAlchemy.fatsrepository import FatsRepository
from src.Application.Fats.Commands.commands import Commands
from mediatr import Mediator

class CommandHandler():
        
    @Mediator.handler
    def InsertFat(request: Commands.InsertFatCommand):
        fatsRepository = FatsRepository()
        
        if fatsRepository.ExistsByName(request.NombreEspanyol, request.NombreIngles):
            raise ObjectAlreadyExists(f'Fat {request.NombreIngles} already exists')
          
        fat: Fat = Fat.Create(request.IdTipoGrasa,
                              request.NombreEspanyol,
                              request.NombreIngles,
                              request.NombreEuropeo,
                              request.DescripcionEspanyol,
                              request.DescripcionIngles)
        
        fatsRepository.session.add(fat)
        fatsRepository.session.commit()
        
        return request
    
    @Mediator.handler
    def DeleteFat(request: Commands.DeleteFatCommand):
        fatsRepository = FatsRepository()
        
        if not fatsRepository.Exists(request.FatID):
            raise ObjectNotExists(f'Fat {request.FatID} not exists')
        
        fat: Fat = fatsRepository.GetFatByID(request.FatID)
        
        fatsRepository.Delete(fat)
        
        fatsRepository.session.commit()