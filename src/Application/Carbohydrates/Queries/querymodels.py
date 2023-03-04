class QueryModels():
    class GetCarbohydrateByIDQueryModel():
        def __init__(self, carbohydrateID: int): 
            self.CarbohydrateID: int = carbohydrateID
        
    class GetAllCarbohydratesQueryModel():
        pass