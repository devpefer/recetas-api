from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Domain.FatTypes.fattype import FatType
from src.Infrastructure.SQLAlchemy import secrets

class FatTypesRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
    
    def GetFatTypeByID(self,fatTypeID: int) -> FatType:
        query = self.session.query(FatType).get((fatTypeID,))
        return query
        
    def GetAllFatTypes(self) -> list[FatType]:
        query = self.session.query(FatType).all()
        return query
        
    def ExistsByID(self,idFatType) -> bool:
        query = self.session.query(exists().where(FatType.IdTipoGrasa == idFatType)).scalar()
        return query
    
    def ExistsByType(self,type) -> bool:
        query = self.session.query(exists().where(FatType.Tipo == type)).scalar()
        return query
        
    def Delete(self,fatType: FatType):
        self.session.delete(fatType)