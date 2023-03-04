from pydantic import BaseModel

class Commands():
    class InsertRelationshipFoodVitaminCommand(BaseModel):
        FoodID: int
        VitaminID: int
        VitaminInFood: float
        Each: float
        UnitOfMeasure: str
        
    class DeleteRelationshipFoodVitaminCommand():
        def __init__(self, foodID, vitaminID):
            self.FoodID: int = foodID
            self.VitaminID: int = vitaminID