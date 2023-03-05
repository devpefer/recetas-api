from pydantic import BaseModel

class Commands():
    class InsertVitaminCommand(BaseModel):
        IdCategoriaVitamina: int
        NombreEspanyol: str
        NombreIngles: str
        NombreEuropeo: str
        DescripcionEspanyol: str
        DescripcionIngles: str
        
    class DeleteVitaminCommand(BaseModel):
        def __init__(self, vitaminID):
            self.VitaminID = vitaminID