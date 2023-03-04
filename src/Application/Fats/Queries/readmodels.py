class ReadModels():
    class GetFatByIDReadModel():
        def __init__(self, fatID, fatTypeID, spanishName, englishName, europeanName, spanishDescription, englishDescription):
            self.FatID: int = fatID
            self.FatTypeID: int = fatTypeID
            self.SpanishName: str = spanishName
            self.EnglishName: str = englishName
            self.EuropeanName: str = europeanName
            self.SpanishDescription: str = spanishDescription
            self.EnglishDescription: str = englishDescription
        
    class GetAllFatsInFoodReadModel():
        pass