from src.Domain.Minerals.mineral import Mineral

class ReadModels():
    class GetMineralByIDReadModel():
        def __init__(self, mineralID, mineralCategoryID, spanishName, englishName, europeanName, spanishDescription, englishDescription):
            self.MineralID: int = mineralID
            self.MineralCategoryID: int = mineralCategoryID
            self.SpanishName: str = spanishName
            self.EnglishName: str = englishName
            self.EuropeanName: str = europeanName
            self.SpanishDescription: str = spanishDescription
            self.EnglishDescription: str = englishDescription
        
    class GetAllMineralsReadModel():
        pass
    