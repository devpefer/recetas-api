from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.Domain.Vitamins.vitamin import Vitamin
from src.Infrastructure.SQLAlchemy.vitaminsrepository import VitaminsRepository
from src.Application.Vitamins.Commands.commands import Commands
from mediatr import Mediator

class CommandHandler():
        
    @Mediator.handler
    def InsertVitamin(request: Commands.InsertVitaminCommand):
        vitaminsRepository = VitaminsRepository()
        
        vitamin = Vitamin.Create(request.IdCategoriaVitamina,
                                 request.NombreEspanyol,
                                 request.NombreIngles,
                                 request.NombreEuropeo,
                                 request.DescripcionEspanyol,
                                 request.DescripcionIngles)
        
        vitaminsRepository.session.add(vitamin)
        vitaminsRepository.session.commit()
        
    @Mediator.handler
    def DeleteVitamin(request: Commands.DeleteVitaminCommand):
        vitaminsRepository = VitaminsRepository()
        
        if not vitaminsRepository.Exists(request.VitaminID):
            raise ObjectNotExists(f'Mineral {request.VitaminID} not exists')
        
        vitamin = vitaminsRepository.GetVitaminByID(request.VitaminID)
        
        vitaminsRepository.Delete(vitamin)
        vitaminsRepository.session.commit()