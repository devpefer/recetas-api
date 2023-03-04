from pydantic import BaseModel

class Commands():
    class InsertFatCommand(BaseModel):
        IdTipoGrasa: int
        NombreEspanyol: str
        NombreIngles: str
        NombreEuropeo: str
        DescripcionEspanyol: str
        DescripcionIngles: str
        
    class DeleteFatCommand():
        def __init__(self,fatID):
            self.FatID: int = fatID