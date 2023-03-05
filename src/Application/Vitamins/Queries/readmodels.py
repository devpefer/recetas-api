from src.Domain.Vitamins.vitamin import Vitamin

class ReadModels():
    class GetVitaminByIDReadModel():
        def __init__(
            self,
            vitaminID,
            vitaminCategoryID,
            spanishName,
            englishName,
            europeanName, 
            spanishDescription,
            englishDescription):
            
            self.VitaminID: int = vitaminID
            self.VitaminCategoryID: int = vitaminCategoryID
            self.SpanishName: str = spanishName
            self.EnglishName: str = englishName
            self.EuropeanName: str = europeanName
            self.SpanishDescription: str = spanishDescription
            self.EnglishDescription: str = englishDescription
        
    class GetAllVitaminsReadModel():
        pass
    