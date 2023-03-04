from src.Domain.Relationship_Food_Carbohydrates.relationship_food_carbohydrate import RelationshipFoodCarbohydrate


class ReadModels():
    class GetRelationshipFoodCarbohydrateByIDReadModel():
        def __init__(self, foodID, carbohydrateID, carbohydrateInFood, each, unitOfMeasure):
            self.FoodID: int = foodID
            self.CarbohydrateID: int = carbohydrateID
            self.CarbohydratesInFood: float = carbohydrateInFood
            self.Each: float = each
            self.UnitOfMeasure: str = unitOfMeasure
        
    class GetAllCarbohydratesInFoodReadModel():
        pass