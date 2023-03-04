class ReadModels():
    class GetFatSubtypeByIDReadModel():
        def __init__(self, fatSubtypeID, fatTypeID, subtype, description):
            self.FatSubtypeID: int = fatSubtypeID
            self.FatTypeID: int = fatTypeID
            self.Subtype: str = subtype
            self.Description: str = description
        
    class GetAllFatSubtypesReadModel():
        pass