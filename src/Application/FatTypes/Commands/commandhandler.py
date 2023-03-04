from src.exceptions import ObjectAlreadyExists, ObjectNotExists
from src.Domain.FatTypes.fattype import FatType
from src.Infrastructure.SQLAlchemy.fattypesrepository import FatTypesRepository
from src.Application.FatTypes.Commands.commands import Commands
from mediatr import Mediator

class CommandHandler():
        
    @Mediator.handler
    def InsertFatSubtype(request: Commands.InsertFatTypeCommand):
        fatTypesRepository = FatTypesRepository()
        
        if fatTypesRepository.ExistsByType(request.Type):
            raise ObjectAlreadyExists(f'FatType {request.Type} already exists')
          
        fatType: FatType = FatType.Create(request.Type,request.Description)
        
        fatTypesRepository.session.add(fatType)
        fatTypesRepository.session.commit()
        
    @Mediator.handler
    def Delete(request: Commands.DeleteFatTypeCommand):
        fatTypesRepository = FatTypesRepository()
        
        if not fatTypesRepository.ExistsByID(request.FatTypeID):
            raise ObjectNotExists(f'FatType {request.FatTypeID} not exists')
        
        fatType: FatType = fatTypesRepository.GetFatTypeByID(request.FatTypeID)
        
        fatTypesRepository.Delete(fatType)
        
        fatTypesRepository.session.commit()
        