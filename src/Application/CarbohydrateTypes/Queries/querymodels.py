class QueryModels():
    class GetCarbohydrateTypeByIDQueryModel():
        def __init__(self, carbohydrateTypeID):
            self.CarbohydrateTypeID: int = carbohydrateTypeID
            
    class GetAllCarbohydrateTypesQueryModel:
        pass