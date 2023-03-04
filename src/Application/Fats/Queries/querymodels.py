class QueryModels():
    class GetFatByIDQueryModel():
        def __init__(self,fatID):
            self.FatID: int = fatID
            
    class GetAllFatsQueryModel():
        pass