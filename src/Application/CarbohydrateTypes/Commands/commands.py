from pydantic import BaseModel

class Commands():
    class InsertCarbohydrateTypeCommand(BaseModel):
        Tipo: int
        Descripcion: str
        
    class DeleteCarbohydrateTypeCommand():
        def __init__(self, carbohydrateTypeID):
            self.CarbohydrateTypeID = carbohydrateTypeID