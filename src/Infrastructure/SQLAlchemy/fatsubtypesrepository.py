from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.FatSubtypes.Commands.commands import Commands
from src.Domain.FatSubtypes.fatsubtype import FatSubtype
from src.Infrastructure.SQLAlchemy import secrets

class FatSubtypesRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
    
    def GetFatSubtypeByID(self,fatSubtypeID: int) -> FatSubtype:
        query = self.session.query(FatSubtype).get((fatSubtypeID,))
        return query
        
    def GetAllFatSubtypes(self) -> list[FatSubtype]:
        query = self.session.query(FatSubtype).all()
        return query
        
    def ExistsByID(self,idFatSubtype) -> bool:
        query = self.session.query(exists().where(FatSubtype.IdSubtipoGrasa == idFatSubtype)).scalar()
        return query
    
    def ExistsBySubtype(self,subtype) -> bool:
        query = self.session.query(exists().where(FatSubtype.Subtipo == subtype)).scalar()
        return query
        
    def Delete(self,fatSubtype: FatSubtype):
        self.session.delete(fatSubtype)