from src.Domain.Relationship_Food_Carbohydrates.relationship_food_carbohydrate import RelationshipFoodCarbohydrate
from src.Infrastructure.SQLAlchemy.relationshipfoodcarbohydraterepository import RelationshipFoodCarbohydrateRepository
from src.Application.Food.Queries.querymodels import QueryModels
from src.Application.Food.Commands.commands import FoodCommands
from src.Application.Relationship_Food_Carbohydrates.Commands.commands import Commands
from src.Domain.Food.food import Food
from src.Application.Food.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.foodrepository import FoodRepository

class FoodQueryHandler():
    def __init__(self):
        self.foodRepository = FoodRepository()
        self.relationshipFoodCarbohydrate = RelationshipFoodCarbohydrateRepository()
        
    def GetFoodByID(self, foodByIDQueryModel: QueryModels.GetFoodByIDQueryModel) -> ReadModels.GetFoodByIDReadModel:
        #Esto para cuando tenga todo en la BBDD
        food = self.foodRepository.GetFoodByID(foodByIDQueryModel.FoodID)
    
        foodReadModel = ReadModels.GetFoodByIDReadModel()
        foodReadModel.FoodID = food.IDIngrediente
        foodReadModel.FoodTypeID = food.IDIngredienteTipo
        foodReadModel.Name = food.NombreIngrediente
        foodReadModel.Description = food.DescripcionIngrediente
        
        return foodReadModel
    