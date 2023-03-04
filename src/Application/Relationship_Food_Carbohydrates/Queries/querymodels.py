class QueryModels():
    class GetRelationshipFoodCarbohydrateByIDQueryModel():
        def __init__(self, foodID,carbohydrateID):
            self.FoodID: int = foodID
            self.CarbohydrateID: int = carbohydrateID
        
    class GetAllCarbohydratesInFoodQueryModel():
        def __init__(self, foodID):
            self.FoodID: int = foodID