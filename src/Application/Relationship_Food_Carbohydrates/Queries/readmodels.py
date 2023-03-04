from src.Domain.Relationship_Food_Carbohydrates.relationship_food_carbohydrate import RelationshipFoodCarbohydrate

class ReadModels():
    class GetRelationshipFoodCarbohydrateByIDReadModel():
        def __init__(self, idIngrediente, idHidratoDeCarbono, cantidadHidratoDeCarbonoEnIngrediente, porCada, unidadMedidaHidratoDeCarbonoEnIngrediente):
            self.IdIngrediente: int = idIngrediente
            self.IdHidratoDeCarbono: int = idHidratoDeCarbono
            self.CantidadHidratoDeCarbonoEnIngrediente: float = float(cantidadHidratoDeCarbonoEnIngrediente)
            self.PorCada: float = porCada
            self.UnidadMedidaHidratoDeCarbonoEnIngrediente: str = unidadMedidaHidratoDeCarbonoEnIngrediente
        
    class GetAllCarbohydratesInFoodReadModel():
        pass