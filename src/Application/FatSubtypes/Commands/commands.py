from pydantic import BaseModel

class Commands():
    class InsertFatSubtypeCommand(BaseModel):
        FatTypeID: int
        Subtype: str
        Description: str
        
    class DeleteFatSubtypeCommand():
        def __init__(self, fatSubtypeID: int):
            self.FatSubtypeID: int = fatSubtypeID