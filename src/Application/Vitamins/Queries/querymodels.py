class QueryModels():
    class GetVitaminByIDQueryModel():
        def __init__(self, vitaminID):
            self.VitaminID: int = vitaminID
        
    class GetAllVitaminsQueryModel():
        pass