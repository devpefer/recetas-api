from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.Domain.Minerals.mineral import Mineral
from src.Infrastructure.SQLAlchemy.mineralsrepository import MineralsRepository
from src.Application.Minerals.Commands.commands import Commands
from mediatr import Mediator

class CommandHandler():
        
    @Mediator.handler
    def InsertMineral(request: Commands.InsertMineralCommand):
        mineralsRepository = MineralsRepository()
        
        mineral = Mineral.Create(request.IdCategoriaMineral,
                                 request.NombreEspanyol,
                                 request.NombreIngles,
                                 request.NombreEuropeo,
                                 request.DescripcionEspanyol,
                                 request.DescripcionIngles)
        
        mineralsRepository.session.add(mineral)
        mineralsRepository.session.commit()
        
    @Mediator.handler
    def DeleteMineral(request: Commands.DeleteMineralCommand):
        mineralsRepository = MineralsRepository()
        
        if not mineralsRepository.Exists(request.MineralID):
            raise ObjectNotExists(f'Mineral {request.MineralID} not exists')
        
        mineral = mineralsRepository.GetMineralByID(request.MineralID)
        
        mineralsRepository.Delete(mineral)
        mineralsRepository.session.commit()