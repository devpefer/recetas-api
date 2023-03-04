from src.Domain.CarbohydrateTypes.carbohydratetypes import CarbohydrateType

class ReadModels():
    class GetCarbohydrateTypeByIDReadModel():
        def __init__(self, carbohydrateTypeID: int, type: int, description: str):
            self.CarbohydrateTypeID: int = carbohydrateTypeID
            self.Type: int = type
            self.Description: str = description
        
    class GetAllCarbohydrateTypesReadModel():
        pass