from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Domain.CarbohydrateTypes.carbohydratetypes import CarbohydrateType
from src.Infrastructure.SQLAlchemy import secrets

class CarbohydrateTypesRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
    
    def GetCarbohydrateTypeByID(self,carbohydrateTypeID: int) -> CarbohydrateType:
        query = self.session.query(CarbohydrateType).get((carbohydrateTypeID,))
        return query
        
    def GetAllCarbohydrateTypes(self) -> list[CarbohydrateType]:
        query = self.session.query(CarbohydrateType).all()
        return query
        
    def Exists(self,idTipoHidratoDeCarbono) -> bool:
        query = self.session.query(exists().where(CarbohydrateType.IdTipoHidratoDeCarbono == idTipoHidratoDeCarbono)).scalar()
        return query
    
    def ExistsByName(self,type) -> bool:
        query = self.session.query(exists().where(CarbohydrateType.Tipo == type)).scalar()
        return query
        
    def Delete(self,carbohydrateType: CarbohydrateType):
        self.session.delete(carbohydrateType)