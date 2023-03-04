class ReadModels():
    class GetCarbohydrateByIDReadModel():
        def __init__(self, carbohydrateID, carbohydrateTypeID, spanishName, englishName, europeanName, spanishDescription, englishDescription):
            self.CarbohydrateID: int = carbohydrateID
            self.CarbohydrateTypeID: int = carbohydrateTypeID
            self.SpanishName: str = spanishName
            self.EnglishName: str = englishName
            self.EuropeanName: str = europeanName
            self.SpanishDescription: str = spanishDescription
            self.EnglishDescription: str = englishDescription
        
    class GetAllCarbohydratesReadModel():
        pass