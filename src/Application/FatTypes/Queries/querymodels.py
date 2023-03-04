class QueryModels():
    class GetFatTypeByIDQueryModel():
        def __init__(self, fatTypeID):
            self.FatTypeID: int = fatTypeID
        
    class GetAllFatTypesQueryModel():
        pass