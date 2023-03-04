class ReadModels():
    class GetFoodByIDReadModel():
        FoodID: str
        FoodTypeID: str
        Name: str
        Description: str
        
    class GetBEDCAFoodByFoodIDReadModel():
        class GetBEDCAInfoByFoodIDReadModel():
            NameSpanish: str
            NameEnglish: str
            NameEuropean: str
            DescriptionSpanish: str
            DescriptionEnglish: str
            GroupSpanish: str
            GroupEnglish: str
            EveryOneHundredGrams: str
            MeasureUnit: str
            MeasureUnitDescriptionSpanish: str
            MeasureUnitDescriptionEnglish: str
            MUnitDescriptionSpanish: str
            MUnitDescriptionEnglish: str
            ValueType: str
        FoodType: str = None
        FoodTypeGroup: str = None
        NameSpanish: str = None
        NameEnglish: str = None
        ScientificName: str = None
        DescriptionSpanish: str = None
        DescriptionEnglish: str = None
        Fats: GetBEDCAInfoByFoodIDReadModel = None
        Protein: GetBEDCAInfoByFoodIDReadModel = None
        Water: GetBEDCAInfoByFoodIDReadModel = None
        Carbohydrates: GetBEDCAInfoByFoodIDReadModel = None
        Fiber: GetBEDCAInfoByFoodIDReadModel = None
        Starch: GetBEDCAInfoByFoodIDReadModel = None
        MonounsaturatedFattyAcids: GetBEDCAInfoByFoodIDReadModel = None
        PoliunsaturatedFattyAcids: GetBEDCAInfoByFoodIDReadModel = None
        SaturatedFattyAcids: GetBEDCAInfoByFoodIDReadModel = None
        Cholesterol: GetBEDCAInfoByFoodIDReadModel = None
        VitaminA: GetBEDCAInfoByFoodIDReadModel = None
        VitaminB6: GetBEDCAInfoByFoodIDReadModel = None
        VitaminB12: GetBEDCAInfoByFoodIDReadModel = None
        VitaminC: GetBEDCAInfoByFoodIDReadModel = None
        VitaminD: GetBEDCAInfoByFoodIDReadModel = None
        VitaminE: GetBEDCAInfoByFoodIDReadModel = None
        Niacin: GetBEDCAInfoByFoodIDReadModel = None
        Riboflavin: GetBEDCAInfoByFoodIDReadModel = None
        Thiamin: GetBEDCAInfoByFoodIDReadModel = None
        Pyridoxine: GetBEDCAInfoByFoodIDReadModel = None
        Calcium: GetBEDCAInfoByFoodIDReadModel = None
        Iron: GetBEDCAInfoByFoodIDReadModel = None
        Potassium: GetBEDCAInfoByFoodIDReadModel = None
        Magnesium: GetBEDCAInfoByFoodIDReadModel = None
        Sodium: GetBEDCAInfoByFoodIDReadModel = None
        Phosphorus: GetBEDCAInfoByFoodIDReadModel = None
        Iodide: GetBEDCAInfoByFoodIDReadModel = None
        Selenium: GetBEDCAInfoByFoodIDReadModel = None
        Zinc: GetBEDCAInfoByFoodIDReadModel = None
        
    class GetBEDCAInfoByFoodIDReadModel():
        NameSpanish: str
        NameEnglish: str
        NameEuropean: str
        DescriptionSpanish: str
        DescriptionEnglish: str
        GroupSpanish: str
        GroupEnglish: str
        EveryOneHundredGrams: str
        MeasureUnit: str
        MeasureUnitDescriptionSpanish: str
        MeasureUnitDescriptionEnglish: str
        MUnitDescriptionSpanish: str
        MUnitDescriptionEnglish: str
        ValueType: str