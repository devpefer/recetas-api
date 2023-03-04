from src.Domain.Relationship_Food_Vitamins.relationship_food_vitamin import RelationshipFoodVitamin

class ReadModels():
    class GetRelationshipFoodVitaminByIDReadModel():
        def __init__(self, idIngrediente, idVitamina, cantidadVitaminaEnIngrediente, porCada, unidadMedidaVitaminaEnIngrediente):
            self.IdIngrediente: int = idIngrediente
            self.IdVitamina: int = idVitamina
            self.CantidadVitaminaEnIngrediente: float = float(cantidadVitaminaEnIngrediente)
            self.PorCada: float = porCada
            self.UnidadMedidaVitaminaEnIngrediente: str = unidadMedidaVitaminaEnIngrediente
        
    class GetAllVitaminsInFoodReadModel():
        pass