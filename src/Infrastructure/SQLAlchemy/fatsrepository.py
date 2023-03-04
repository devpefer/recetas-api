from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Fats.Commands.commands import Commands
from src.Domain.Fats.fat import Fat
from src.Infrastructure.SQLAlchemy import secrets

class FatsRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
    
    def GetFatByID(self,fatID: int) -> Fat:
        query = self.session.query(Fat).get((fatID,))
        return query
        
    def GetAllFats(self) -> list[Fat]:
        query = self.session.query(Fat).all()
        return query
        
    def Exists(self,idGrasa) -> bool:
        query = self.session.query(exists().where(Fat.IdGrasa == idGrasa)).scalar()
        return query
    
    def ExistsByName(self,spanishName, englishName: int) -> bool:
        query = self.session.query(exists().where(Fat.NombreEspanyol == spanishName, Fat.NombreIngles == englishName)).scalar()
        return query
        
    def Delete(self,fat: Fat):
        self.session.delete(fat)