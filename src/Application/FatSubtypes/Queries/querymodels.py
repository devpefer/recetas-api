class QueryModels():
    class GetFatSubtypeByIDQueryModel():
        def __init__(self, fatSubtypeID):
            self.FatSubtypeID: int = fatSubtypeID
            
    class GetAllFatSubtypesQueryModel():
        pass