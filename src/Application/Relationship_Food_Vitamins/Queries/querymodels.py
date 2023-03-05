class QueryModels():
    class GetRelationshipFoodVitaminByIDQueryModel():
        def __init__(self, foodID,vitaminID):
            self.FoodID: int = foodID
            self.VitaminID: int = vitaminID
        
    class GetAllVitaminsInFoodQueryModel():
        def __init__(self, foodID):
            self.FoodID: int = foodID