from pydantic import BaseModel

class Commands():
    class InsertFatTypeCommand(BaseModel):
        Type: str
        Description: str
        
    class DeleteFatTypeCommand():
        def __init__(self, fatTypeID):
            self.FatTypeID: int = fatTypeID