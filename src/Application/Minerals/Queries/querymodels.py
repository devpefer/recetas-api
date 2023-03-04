class QueryModels():
    class GetMineralByIDQueryModel():
        def __init__(self, mineralID):
            self.MineralID: int = mineralID
        
    class GetAllMineralsQueryModel():
        pass