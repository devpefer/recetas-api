from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.Domain.FatSubtypes.fatsubtype import FatSubtype
from src.Infrastructure.SQLAlchemy.fatsubtypesrepository import FatSubtypesRepository
from src.Application.FatSubtypes.Commands.commands import Commands
from mediatr import Mediator

class CommandHandler():
        
    @Mediator.handler
    def InsertFatSubtype(request: Commands.InsertFatSubtypeCommand):
        fatSubtypesRepository = FatSubtypesRepository()
        
        if fatSubtypesRepository.ExistsBySubtype(request.Subtype):
            raise ObjectAlreadyExists(f'FatSubtype {request.Subtype} already exists')
          
        fatSubtype: FatSubtype = FatSubtype.Create(request.FatTypeID,request.Subtype,request.Description)
        
        fatSubtypesRepository.session.add(fatSubtype)
        fatSubtypesRepository.session.commit()
        
    @Mediator.handler
    def DeleteFatSubtype(request: Commands.DeleteFatSubtypeCommand):
        fatSubtypesRepository = FatSubtypesRepository()
        
        if not fatSubtypesRepository.ExistsByID(request.FatSubtypeID):
            raise ObjectNotExists(f'FatSubtype {request.FatSubtypeID} not exists')
        
        fatSubtype: FatSubtype = fatSubtypesRepository.GetFatSubtypeByID(request.FatSubtypeID)
        
        fatSubtypesRepository.Delete(fatSubtype)
        
        fatSubtypesRepository.session.commit()
        