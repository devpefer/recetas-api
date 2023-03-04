from pydantic import BaseModel

class Commands():
    class InsertMineralCommand(BaseModel):
        IdCategoriaMineral: int
        NombreEspanyol: str
        NombreIngles: str
        NombreEuropeo: str
        DescripcionEspanyol: str
        DescripcionIngles: str
        
    class DeleteMineralCommand(BaseModel):
        def __init__(self, mineralID):
            self.MineralID = mineralID