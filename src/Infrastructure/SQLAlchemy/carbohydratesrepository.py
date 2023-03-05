from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Domain.Carbohydrates.carbohydrate import Carbohydrate
from src.Infrastructure.SQLAlchemy import secrets

class CarbohydratesRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
    
    def GetCarbohydrateByID(self,carbohydrateID: int) -> Carbohydrate:
        query = self.session.query(Carbohydrate).get((carbohydrateID,))
        return query
        
    def GetAllCarbohydrates(self) -> list[Carbohydrate]:
        query = self.session.query(Carbohydrate).all()
        return query
        
    def Exists(self,idHidratoDeCarbono) -> bool:
        query = self.session.query(exists().where(Carbohydrate.IdHidratoDeCarbono == idHidratoDeCarbono)).scalar()
        return query
    
    def ExistsByName(self,spanishName, englishName: int) -> bool:
        query = self.session.query(exists().where(Carbohydrate.NombreEspanyol == spanishName, Carbohydrate.NombreIngles == englishName)).scalar()
        return query
        
    def Delete(self,carbohydrate: Carbohydrate):
        self.session.delete(carbohydrate)