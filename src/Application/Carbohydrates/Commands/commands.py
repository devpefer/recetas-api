from pydantic import BaseModel

class Commands():
    class InsertCarbohydrateCommand(BaseModel):
        IdTipoHidratoDeCarbono: int
        NombreEspanyol: str
        NombreIngles: str
        NombreEuropeo: str
        DescripcionEspanyol: str
        DescripcionIngles: str

    class DeleteCarbohydrateCommand():
        def __init__(self, carbohydrateID: int):
            self.IdHidratoDeCarbono: int = carbohydrateID