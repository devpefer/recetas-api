class ReadModels():
    class GetFatTypeByIDReadModel():
        def __init__(self, fatTypeID, type, description):
            self.FatTypeID: int = fatTypeID
            self.Type: str = type
            self.Description: str = description
        