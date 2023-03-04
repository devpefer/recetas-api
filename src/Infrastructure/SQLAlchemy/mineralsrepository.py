from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Minerals.Commands.commands import Commands
from src.Domain.Minerals.mineral import Mineral
from src.Infrastructure.SQLAlchemy import secrets

class MineralsRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
    
    def GetMineralByID(self,mineralID: int) -> Mineral:
        query = self.session.query(Mineral).get((mineralID,))
        return query
        
    def GetAllMinerals(self) -> list[Mineral]:
        query = self.session.query(Mineral).all()
        return query
        
    def Exists(self,idMineral) -> bool:
        query = self.session.query(exists().where(Mineral.IdMineral == idMineral)).scalar()
        return query
        
    def Delete(self,mineral: Mineral):
        self.session.delete(mineral)