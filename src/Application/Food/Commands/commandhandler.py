from src.Domain.Food.food import Food
from src.Infrastructure.SQLAlchemy.foodrepository import FoodRepository
from src.Application.Food.Commands.commands import FoodCommands

class CommandHandler():
    def __init__(self):
        self.foodRepository = FoodRepository()
        
    def InsertFood(self,command: FoodCommands.InsertFoodCommand):
        if self.foodRepository.Exists(command.FoodID):
            raise Exception(f'Food {command.FoodID} already exists')
        
        food = Food.Create(self,command)
        
        self.foodRepository.session.add(food)
        self.foodRepository.session.commit()
        
        return command
        
    def ModifyName(self,command: FoodCommands.ModifyFoodNameCommand):   
        if not self.foodRepository.Exists(command.FoodID):
            raise Exception(f'Food {command.FoodID} not exists')
        
        food = self.foodRepository.GetFoodByID(command.FoodID)
        
        food.ModifyName(command.NewName)
        
        self.foodRepository.session.commit()

        return command
        
    def ModifyDescription(self,command: FoodCommands.ModifyFoodDescriptionCommand):   
        if not self.foodRepository.Exists(command.FoodID):
            raise Exception(f'Food {command.FoodID} not exists')
        
        food = self.foodRepository.GetFoodByID(command.FoodID)
        
        food.ModifyDescription(command.NewDescription)
        
        self.foodRepository.session.commit()
        
        return command
        
    def Delete(self,foodID):   
        if not self.foodRepository.Exists(foodID):
            raise Exception(f'Food {foodID} not exists')
        
        food = self.foodRepository.GetFoodByID(foodID)
        
        self.foodRepository.Delete(food)
        
        self.foodRepository.session.commit()