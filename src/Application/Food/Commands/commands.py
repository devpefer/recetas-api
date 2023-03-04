from pydantic import BaseModel

class FoodCommands():
    class InsertFoodCommand():
        """Inserts a food

        Args:
            BaseModel (_type_): _description_
        """
        def __init__(self, foodTypeID, foodName, foodDescription):
            self.FoodTypeID = foodTypeID
            self.FoodName = foodName
            self.FoodDescription = foodDescription
        
    class ModifyFoodNameCommand(BaseModel):
        """Modifies the name of a food

        Args:
            BaseModel (_type_): _description_
        """
        FoodID: str
        NewName: str
        
    class ModifyFoodDescriptionCommand(BaseModel):
        """Modifies the description of a food 

        Args:
            BaseModel (_type_): _description_
        """
        FoodID: str
        NewDescription: str