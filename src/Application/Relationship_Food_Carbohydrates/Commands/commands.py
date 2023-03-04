from pydantic import BaseModel

class Commands():
    class InsertRelationshipFoodCarbohydrateCommand(BaseModel):
        FoodID: int
        CarbohydrateID: int
        CarbohydrateInFood: float
        Each: float
        UnitOfMeasure: str
        
    class DeleteRelationshipFoodCarbohydrateCommand():
        def __init__(self, foodID, carbohydrateID):
            self.FoodID: int = foodID
            self.CarbohydrateID: int = carbohydrateID