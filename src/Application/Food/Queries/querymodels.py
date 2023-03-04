from pydantic import BaseModel

class QueryModels():
    class GetFoodByIDQueryModel(BaseModel):
        FoodID: int
        