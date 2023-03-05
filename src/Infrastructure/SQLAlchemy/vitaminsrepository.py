from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Vitamins.Commands.commands import Commands
from src.Domain.Vitamins.vitamin import Vitamin
from src.Infrastructure.SQLAlchemy import secrets

class VitaminsRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
    
    def GetVitaminByID(self,vitaminID: int) -> Vitamin:
        query = self.session.query(Vitamin).get((vitaminID,))
        return query
        
    def GetAllVitamins(self) -> list[Vitamin]:
        query = self.session.query(Vitamin).all()
        return query
        
    def Exists(self,idVitamina) -> bool:
        query = self.session.query(exists().where(Vitamin.IdVitamina == idVitamina)).scalar()
        return query
        
    def Delete(self,vitamin: Vitamin):
        self.session.delete(vitamin)