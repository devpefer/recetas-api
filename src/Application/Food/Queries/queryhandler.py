import os
from src.Domain.Relationship_Food_Carbohydrates.relationship_food_carbohydrate import RelationshipFoodCarbohydrate
from src.Infrastructure.SQLAlchemy.relationshipfoodcarbohydraterepository import RelationshipFoodCarbohydrateRepository
from src.Application.Food.Queries.querymodels import QueryModels
from src.Application.Food.Commands.commands import FoodCommands
from src.Application.Relationship_Food_Carbohydrates.Commands.commands import Commands
from src.Domain.Food.food import Food
from src.Application.Food.Queries.readmodels import ReadModels
from src.Infrastructure.SQLAlchemy.foodrepository import FoodRepository
from src.BedcaClient import BedcaClient
import json

class FoodQueryHandler():
    def __init__(self):
        self.foodRepository = FoodRepository()
        self.relationshipFoodCarbohydrate = RelationshipFoodCarbohydrateRepository()
        
    def GetFoodByID(self, foodByIDQueryModel: QueryModels.GetFoodByIDQueryModel) -> ReadModels.GetFoodByIDReadModel:
        #Esto para cuando tenga todo en la BBDD
        food = self.foodRepository.GetFoodByID(foodByIDQueryModel.FoodID)
    
        foodReadModel = ReadModels.GetFoodByIDReadModel()
        foodReadModel.FoodID = food.IDIngrediente
        foodReadModel.FoodTypeID = food.IDIngredienteTipo
        foodReadModel.Name = food.NombreIngrediente
        foodReadModel.Description = food.DescripcionIngrediente
        
        #De momento utilizamos BedcaClient
        #bedcaClient = BedcaClient()
        #food = json.loads(bedcaClient.getFood(foodByIDQueryModel))
        # 
        #foodReadModel = ReadModels.GetFoodByIDReadModel()
        #foodReadModel.FoodID = food['foodresponse']['food']['f_id']
        #foodReadModel.FoodTypeID = ''
        #foodReadModel.Name = food['foodresponse']['food']['f_ori_name']
        #foodReadModel.Description = ''
        
        return foodReadModel
    
    def DownloadAllFoodsToJSON(self) -> int:
        status = 0
        
        bedcaClient = BedcaClient()
        
        try:
            for i in range(5000):
                food = dict(json.loads(bedcaClient.getFood(i)))
        
                with open(f'/home/devpefer/BEDCARESPONSES/{i}.json', mode = 'w', encoding = 'UTF-8') as file:
                    json.dump(food, file)
        except:
            status = 1
        
        return status 
    
    def GetAllFood(self,jsonFiles: list[str]) -> list[ReadModels.GetBEDCAFoodByFoodIDReadModel]:
        listFood = []
        listFats = []
        contRegistros = 0
        for fileName in jsonFiles:
            try:
                pathToFile = f'/Users/devpefer/BEDCARESPONSES/{fileName}'
                with open(pathToFile,mode='r') as file:
                    jsonString = file.read()
                    jsonFile = json.loads(jsonString)
                    food = ReadModels.GetBEDCAFoodByFoodIDReadModel()
                    
                    food.FoodType = jsonFile['foodresponse']['food']['namelevel2']
                    food.FoodTypeGroup = jsonFile['foodresponse']['food']['namelevel1']
                    food.NameSpanish = jsonFile['foodresponse']['food']['f_ori_name']
                    food.NameEnglish = jsonFile['foodresponse']['food']['f_eng_name']
                    food.ScientificName = jsonFile['foodresponse']['food']['sci_name']
                    listFood.append(food)
                    
                    #foodValues = len(jsonFile['foodresponse']['food']['foodvalue'])
                    #for foodValue in range(foodValues):
                    #    fats = ReadModels.GetBEDCAFatsByFoodIDReadModel()
                    #    fats.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][foodValue]['c_ori_name']
                    #    fats.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][foodValue]['c_eng_name']
                    #    listFats.append(fats)
                    #    food.ListFats = listFats
                    
                    for i in range(len(jsonFile['foodresponse']['food']['foodvalue'])):
                        try:
                            if (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '410'):
                                fats = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                fats.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                fats.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                fats.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                fats.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                fats.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                fats.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                fats.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                fats.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                fats.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                fats.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                fats.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Fats = fats
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '416'):
                                protein = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                protein.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                protein.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                protein.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                protein.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                protein.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                protein.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                protein.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                protein.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                protein.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                protein.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                protein.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Protein = protein
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '417'):
                                water = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                water.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                water.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                water.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                water.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                water.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                water.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                water.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                water.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                water.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                water.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                water.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Water = water
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '53'):
                                carbohydrates = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                carbohydrates.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                carbohydrates.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                carbohydrates.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                carbohydrates.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                carbohydrates.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                carbohydrates.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                carbohydrates.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                carbohydrates.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                carbohydrates.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                carbohydrates.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                carbohydrates.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Carbohydrates = carbohydrates
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '307'):
                                fiber = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                fiber.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                fiber.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                fiber.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                fiber.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                fiber.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                fiber.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                fiber.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                fiber.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                fiber.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                fiber.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                fiber.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Fiber = fiber
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '423'):
                                starch = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                starch.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                starch.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                starch.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                starch.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                starch.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                starch.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                starch.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                starch.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                starch.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                starch.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                starch.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Starch = starch
                            
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '282'):
                                monounsaturatedFattyAcids = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                monounsaturatedFattyAcids.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                monounsaturatedFattyAcids.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                monounsaturatedFattyAcids.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                monounsaturatedFattyAcids.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                monounsaturatedFattyAcids.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                monounsaturatedFattyAcids.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                monounsaturatedFattyAcids.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                monounsaturatedFattyAcids.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                monounsaturatedFattyAcids.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                monounsaturatedFattyAcids.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                monounsaturatedFattyAcids.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.MonounsaturatedFattyAcids = monounsaturatedFattyAcids
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '287'):
                                poliunsaturatedFattyAcids = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                poliunsaturatedFattyAcids.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                poliunsaturatedFattyAcids.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                poliunsaturatedFattyAcids.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                poliunsaturatedFattyAcids.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                poliunsaturatedFattyAcids.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                poliunsaturatedFattyAcids.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                poliunsaturatedFattyAcids.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                poliunsaturatedFattyAcids.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                poliunsaturatedFattyAcids.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                poliunsaturatedFattyAcids.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                poliunsaturatedFattyAcids.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.PoliunsaturatedFattyAcids = poliunsaturatedFattyAcids
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '299'):
                                saturatedFattyAcids = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                saturatedFattyAcids.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                saturatedFattyAcids.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                saturatedFattyAcids.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                saturatedFattyAcids.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                saturatedFattyAcids.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                saturatedFattyAcids.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                saturatedFattyAcids.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                saturatedFattyAcids.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                saturatedFattyAcids.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                saturatedFattyAcids.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                saturatedFattyAcids.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.SaturatedFattyAcids = saturatedFattyAcids
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '433'):
                                cholesterol = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                cholesterol.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                cholesterol.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                cholesterol.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                cholesterol.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                cholesterol.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                cholesterol.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                cholesterol.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                cholesterol.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                cholesterol.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                cholesterol.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                cholesterol.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Cholesterol = cholesterol
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '103'):
                                vitaminE = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                vitaminE.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                vitaminE.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                vitaminE.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                vitaminE.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                vitaminE.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                vitaminE.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                vitaminE.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                vitaminE.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                vitaminE.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                vitaminE.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                vitaminE.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.VitaminE = vitaminE
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '475'):
                                niacin = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                niacin.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                niacin.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                niacin.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                niacin.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                niacin.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                niacin.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                niacin.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                niacin.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                niacin.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                niacin.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                niacin.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Niacin = niacin
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '482'):
                                riboflavin = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                riboflavin.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                riboflavin.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                riboflavin.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                riboflavin.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                riboflavin.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                riboflavin.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                riboflavin.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                riboflavin.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                riboflavin.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                riboflavin.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                riboflavin.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Riboflavin = riboflavin
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '483'):
                                thiamin = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                thiamin.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                thiamin.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                thiamin.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                thiamin.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                thiamin.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                thiamin.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                thiamin.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                thiamin.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                thiamin.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                thiamin.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                thiamin.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Thiamin = thiamin
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '484'):
                                vitaminB12 = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                vitaminB12.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                vitaminB12.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                vitaminB12.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                vitaminB12.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                vitaminB12.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                vitaminB12.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                vitaminB12.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                vitaminB12.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                vitaminB12.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                vitaminB12.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                vitaminB12.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.VitaminB12 = vitaminB12
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '485'):
                                pyridoxine = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                pyridoxine.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                pyridoxine.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                pyridoxine.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                pyridoxine.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                pyridoxine.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                pyridoxine.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                pyridoxine.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                pyridoxine.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                pyridoxine.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                pyridoxine.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                pyridoxine.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Pyridoxine = pyridoxine
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '100'):
                                vitaminA = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                vitaminA.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                vitaminA.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                vitaminA.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                vitaminA.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                vitaminA.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                vitaminA.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                vitaminA.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                vitaminA.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                vitaminA.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                vitaminA.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                vitaminA.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.VitaminA = vitaminA
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '102'):
                                vitaminD = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                vitaminD.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                vitaminD.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                vitaminD.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                vitaminD.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                vitaminD.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                vitaminD.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                vitaminD.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                vitaminD.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                vitaminD.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                vitaminD.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                vitaminD.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.VitaminD = vitaminD
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '486'):
                                vitaminC = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                vitaminC.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                vitaminC.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                vitaminC.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                vitaminC.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                vitaminC.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                vitaminC.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                vitaminC.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                vitaminC.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                vitaminC.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                vitaminC.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                vitaminC.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.VitaminC = vitaminC
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '317'):
                                calcium = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                calcium.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                calcium.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                calcium.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                calcium.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                calcium.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                calcium.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                calcium.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                calcium.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                calcium.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                calcium.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                calcium.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Calcium = calcium
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '319'):
                                iron = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                iron.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                iron.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                iron.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                iron.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                iron.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                iron.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                iron.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                iron.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                iron.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                iron.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                iron.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Iron = iron
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '321'):
                                potassium = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                potassium.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                potassium.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                potassium.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                potassium.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                potassium.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                potassium.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                potassium.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                potassium.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                potassium.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                potassium.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                potassium.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Potassium = potassium
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '322'):
                                magnesium = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                magnesium.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                magnesium.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                magnesium.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                magnesium.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                magnesium.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                magnesium.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                magnesium.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                magnesium.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                magnesium.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                magnesium.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                magnesium.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Magnesium = magnesium
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '323'):
                                sodium = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                sodium.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                sodium.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                sodium.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                sodium.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                sodium.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                sodium.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                sodium.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                sodium.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                sodium.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                sodium.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                sodium.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Sodium = sodium
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '326'):
                                phosphorus = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                phosphorus.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                phosphorus.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                phosphorus.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                phosphorus.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                phosphorus.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                phosphorus.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                phosphorus.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                phosphorus.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                phosphorus.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                phosphorus.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                phosphorus.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Phosphorus = phosphorus
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '456'):
                                iodide = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                iodide.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                iodide.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                iodide.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                iodide.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                iodide.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                iodide.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                iodide.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                iodide.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                iodide.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                iodide.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                iodide.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Iodide = iodide
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '462'):
                                selenium = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                selenium.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                selenium.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                selenium.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                selenium.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                selenium.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                selenium.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                selenium.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                selenium.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                selenium.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                selenium.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                selenium.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Selenium = selenium
                                
                            elif (jsonFile['foodresponse']['food']['foodvalue'][i]['c_id'] == '464'):
                                zinc = ReadModels.GetBEDCAInfoByFoodIDReadModel()
                                zinc.NameSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_ori_name']
                                zinc.NameEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['c_eng_name']
                                zinc.NameEuropean = jsonFile['foodresponse']['food']['foodvalue'][i]['eur_name']
                                zinc.DescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_esp']
                                zinc.DescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['glos_ing']
                                zinc.EveryOneHundredGrams = jsonFile['foodresponse']['food']['foodvalue'][i]['best_location']
                                zinc.MeasureUnit = jsonFile['foodresponse']['food']['foodvalue'][i]['u_id']
                                zinc.MeasureUnitDescriptionSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_descripcion']
                                zinc.MeasureUnitDescriptionEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['u_description']
                                zinc.GroupSpanish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_descripcion']
                                zinc.GroupEnglish = jsonFile['foodresponse']['food']['foodvalue'][i]['cg_description']
                                food.Zinc = zinc
                                
                        except:
                            continue
                        
                    #contRegistros += 1
                    #if contRegistros >= 20:
                    #    break

            except Exception as e:
                continue
                
            #food = Food.Create(insertFoodCommand)
                
        return listFood
    
    def CategorizarAlimentos(self):
        listFiles = os.listdir('/Users/devpefer/BEDCARESPONSES')
        listFood = self.GetAllFood(listFiles)
        
        try:
            #listGrasasSaturadas = (x for x in listFood if not x.SaturatedFattyAcids is None and not x.SaturatedFattyAcids.EveryOneHundredGrams is None)
            #listGrasasSaturadas = (x for x in listGrasasSaturadas if float(x.SaturatedFattyAcids.EveryOneHundredGrams) > 0)
            listaAnimalesLeche = ['Leche', 'leche']
            listaAnimalesYogur = ['Yogur', 'yogur']
            listaAnimalesQueso = ['Queso', 'queso']
            listaAnimalesCarneRoja = ['cerdo','Cerdo','toro','Toro','buey','Buey','pato','Pato','cabra','Cabra','cordero','Cordero']
            listaAnimalesCarneBlanca = ['conejo','Conejo','pollo','Pollo','pavo','Pavo']
            listaAnimalesPescadoAzul = ['Anchoa','anchoa','anguila','Anguila','boqueron','Boqueron','boquerón','Boquerón','arenque','Arenque','atún','Atún','atun','Atun','bonito','Bonito','Chicharro','chicharro','Jurel','jurel','Lamprea','lamprea','pez espada','Pez espada','salmon','Salmon','salmón','Salmón','Sardina','sardina','Caballa','caballa','Verdel','verdel']
            listaAnimalesPescadoBlanco = ['abadejo','Abadejo','Acedía','acedía','Acedia','acedia','Bacaladilla','bacaladilla','Besugo','besugo','Cabracho','cabracho','Cazon','cazon','Cazón','cazón','Congrio','congrio','Gallo','gallo','Gallineta','gallineta','Lenguado','lenguado','Merluza','merluza','Rosada','rosada','Rape','rape','Raya','raya','Rodaballo','rodaballo']
            listaAnimalesPescadoSemigraso = ['Dorada','dorada','Lubina','lubina','Mero','mero','Salmonete','salmonete','Trucha','trucha']
            
            #listaCarneBlanca = (x for x in listFood for carneBlanca in listaAnimalesCarneBlanca if carneBlanca in x.NameSpanish and not 'Leche' in x.NameSpanish and not 'leche' in x.NameSpanish and not 'Queso' in x.NameSpanish and not 'queso' in x.NameSpanish and not 'Huevo' in x.NameSpanish and not 'huevo' in x.NameSpanish or (('Cerdo' in x.NameSpanish or 'cerdo' in x.NameSpanish) and ('lomo' in x.NameSpanish or 'Lomo' in x.NameSpanish) and ('cordero' in x.NameSpanish or 'Cordero' in x.NameSpanish) and ('lechal' in x.NameSpanish or 'Lechal' in x.NameSpanish)))
            #listaCarneRoja = (x for x in listFood for carneRoja in listaAnimalesCarneRoja if carneRoja in x.NameSpanish and not 'Leche' in x.NameSpanish and not 'leche' in x.NameSpanish and not 'Queso' in x.NameSpanish and not 'queso' in x.NameSpanish and not 'Huevo' in x.NameSpanish and not 'huevo' in x.NameSpanish and (((not 'cordero' in x.NameSpanish and not 'Cordero' in x.NameSpanish) and (not 'lechal' in x.NameSpanish and not 'Lechal' in x.NameSpanish)) and ((not 'cerdo' in x.NameSpanish and not 'Cerdo' in x.NameSpanish) and (not 'lomo' in x.NameSpanish and not 'Lomo' in x.NameSpanish))))
            listaLeche = (x for x in listFood for leche in listaAnimalesLeche if leche in x.NameSpanish)
            listaYogur = (x for x in listFood for yogur in listaAnimalesYogur if yogur in x.NameSpanish)
            listaQueso = (x for x in listFood for queso in listaAnimalesQueso if queso in x.NameSpanish)
            listaCarneBlanca = (x for x in listFood for carneBlanca in listaAnimalesCarneBlanca if carneBlanca in x.NameSpanish and not 'Leche' in x.NameSpanish and not 'leche' in x.NameSpanish and not 'Queso' in x.NameSpanish and not 'queso' in x.NameSpanish and not 'Huevo' in x.NameSpanish and not 'huevo' in x.NameSpanish or ((('Cerdo' in x.NameSpanish or 'cerdo' in x.NameSpanish) and ('lomo' in x.NameSpanish or 'Lomo' in x.NameSpanish)) or (('cordero' in x.NameSpanish or 'Cordero' in x.NameSpanish) and ('lechal' in x.NameSpanish or 'Lechal' in x.NameSpanish))))
            listaCarneRoja = (x for x in listFood for carneRoja in listaAnimalesCarneRoja if carneRoja in x.NameSpanish and not 'Leche' in x.NameSpanish and not 'leche' in x.NameSpanish and not 'Queso' in x.NameSpanish and not 'queso' in x.NameSpanish and not 'Huevo' in x.NameSpanish and not 'huevo' in x.NameSpanish and ((not 'cerdo' in x.NameSpanish and not 'Cerdo' in x.NameSpanish) and (not 'lomo' in x.NameSpanish and not 'Lomo' in x.NameSpanish)) and ((not 'cordero' in x.NameSpanish and not 'Cordero' in x.NameSpanish) and (not 'Lechal' in x.NameSpanish and not 'lechal' in x.NameSpanish)))
            listaPescadoAzul = (x for x in listFood for pescadoAzul in listaAnimalesPescadoAzul if pescadoAzul in x.NameSpanish and not 'Queso' in x.NameSpanish and not 'queso' in x.NameSpanish)
            listaPescadoBlanco = (x for x in listFood for pescadoBlanco in listaAnimalesPescadoBlanco if pescadoBlanco in x.NameSpanish and not 'Queso' in x.NameSpanish and not 'queso' in x.NameSpanish)
            listaPescadoSemigraso = (x for x in listFood for pescadoSemigraso in listaAnimalesPescadoSemigraso if pescadoSemigraso in x.NameSpanish and not 'Queso' in x.NameSpanish and not 'queso' in x.NameSpanish)
            
        except Exception as ex:
            print(ex)
        
        food: ReadModels.GetBEDCAFoodByFoodIDReadModel
        print('LECHE')
        for food in listaLeche:
            try:
                insertFoodCommand = FoodCommands.InsertFoodCommand(1,
                                                               food.NameSpanish,
                                                               food.DescriptionSpanish)
                
                tmpFood = Food.Create(insertFoodCommand.FoodTypeID,
                                      insertFoodCommand.FoodName,
                                      insertFoodCommand.FoodDescription)
                
                if not self.foodRepository.ExistsByName(tmpFood.NombreIngrediente):
                    self.foodRepository.session.add(tmpFood)
                    self.foodRepository.session.commit()
                    tmpFood = self.foodRepository.GetLastFoodID()
                
                tmpRelationshipFoodCarbohydrate = RelationshipFoodCarbohydrate.Create(tmpFood.IDIngrediente,
                                                                                      9,
                                                                                      food.Carbohydrates.EveryOneHundredGrams,
                                                                                      100,
                                                                                      food.Carbohydrates.MeasureUnit)
                
                self.relationshipFoodCarbohydrate.session.add(tmpRelationshipFoodCarbohydrate)
                self.relationshipFoodCarbohydrate.session.commit()
                
                print(f'{food.NameSpanish} - {food.SaturatedFattyAcids.NameSpanish} - {food.SaturatedFattyAcids.GroupSpanish} - {food.SaturatedFattyAcids.EveryOneHundredGrams}')
            except Exception as ex:
                pass
            
        print('YOGUR')
        for food in listaYogur:
            try:
                insertFoodCommand = Commands.InsertFoodCommand()
                insertFoodCommand.FoodName = food.NameSpanish
                insertFoodCommand.FoodID = None
                insertFoodCommand.FoodDescription = food.DescriptionSpanish
                insertFoodCommand.FoodTypeID = 2
                tmpFood = Food.Create(Food,insertFoodCommand)
                if not self.foodRepository.ExistsByName(tmpFood.NombreIngrediente):
                    self.foodRepository.session.add(tmpFood)
                    self.foodRepository.session.commit()
                print(f'{food.NameSpanish} - {food.SaturatedFattyAcids.NameSpanish} - {food.SaturatedFattyAcids.GroupSpanish} - {food.SaturatedFattyAcids.EveryOneHundredGrams}')
            except Exception as ex:
                pass
            
        print('QUESO')
        for food in listaQueso:
            try:
                insertFoodCommand = Commands.InsertFoodCommand
                insertFoodCommand.FoodName = food.NameSpanish
                insertFoodCommand.FoodID = None
                insertFoodCommand.FoodDescription = food.DescriptionSpanish
                insertFoodCommand.FoodTypeID = 3
                tmpFood = Food.Create(Food,insertFoodCommand)
                if not self.foodRepository.ExistsByName(tmpFood.NombreIngrediente):
                    self.foodRepository.session.add(tmpFood)
                    self.foodRepository.session.commit()
                print(f'{food.NameSpanish} - {food.SaturatedFattyAcids.NameSpanish} - {food.SaturatedFattyAcids.GroupSpanish} - {food.SaturatedFattyAcids.EveryOneHundredGrams}')
            except Exception as ex:
                pass
            
        print('CARNES BLANCAS')
        for food in listaCarneBlanca:
            try:
                insertFoodCommand = Commands.InsertFoodCommand
                insertFoodCommand.FoodName = food.NameSpanish
                insertFoodCommand.FoodID = None
                insertFoodCommand.FoodDescription = food.DescriptionSpanish
                insertFoodCommand.FoodTypeID = 4
                tmpFood = Food.Create(Food,insertFoodCommand)
                if not self.foodRepository.ExistsByName(tmpFood.NombreIngrediente):
                    self.foodRepository.session.add(tmpFood)
                    self.foodRepository.session.commit()
                print(f'{food.NameSpanish} - {food.SaturatedFattyAcids.NameSpanish} - {food.SaturatedFattyAcids.GroupSpanish} - {food.SaturatedFattyAcids.EveryOneHundredGrams}')
            except Exception as ex:
                pass
        
        print('CARNES ROJAS')
        for food in listaCarneRoja:
            try:
                insertFoodCommand = Commands.InsertFoodCommand
                insertFoodCommand.FoodName = food.NameSpanish
                insertFoodCommand.FoodID = None
                insertFoodCommand.FoodDescription = food.DescriptionSpanish
                insertFoodCommand.FoodTypeID = 5
                tmpFood = Food.Create(Food,insertFoodCommand)
                if not self.foodRepository.ExistsByName(tmpFood.NombreIngrediente):
                    self.foodRepository.session.add(tmpFood)
                    self.foodRepository.session.commit()
                print(f'{food.NameSpanish} - {food.SaturatedFattyAcids.NameSpanish} - {food.SaturatedFattyAcids.GroupSpanish} - {food.SaturatedFattyAcids.EveryOneHundredGrams}')
            except Exception as ex:
                pass
        
        print('PESCADOS BLANCOS')
        for food in listaPescadoBlanco:
            try:
                insertFoodCommand = Commands.InsertFoodCommand
                insertFoodCommand.FoodName = food.NameSpanish
                insertFoodCommand.FoodID = None
                insertFoodCommand.FoodDescription = food.DescriptionSpanish
                insertFoodCommand.FoodTypeID = 6
                tmpFood = Food.Create(Food,insertFoodCommand)
                if not self.foodRepository.ExistsByName(tmpFood.NombreIngrediente):
                    self.foodRepository.session.add(tmpFood)
                    self.foodRepository.session.commit()
                print(f'{food.NameSpanish} - {food.SaturatedFattyAcids.NameSpanish} - {food.SaturatedFattyAcids.GroupSpanish} - {food.SaturatedFattyAcids.EveryOneHundredGrams}')
            except Exception as ex:
                pass
            
        print('PESCADOS SEMIGRASOS')
        for food in listaPescadoSemigraso:
            try:
                insertFoodCommand = Commands.InsertFoodCommand
                insertFoodCommand.FoodName = food.NameSpanish
                insertFoodCommand.FoodID = None
                insertFoodCommand.FoodDescription = food.DescriptionSpanish
                insertFoodCommand.FoodTypeID = 7
                tmpFood = Food.Create(Food,insertFoodCommand)
                if not self.foodRepository.ExistsByName(tmpFood.NombreIngrediente):
                    self.foodRepository.session.add(tmpFood)
                    self.foodRepository.session.commit()
                print(f'{food.NameSpanish} - {food.SaturatedFattyAcids.NameSpanish} - {food.SaturatedFattyAcids.GroupSpanish} - {food.SaturatedFattyAcids.EveryOneHundredGrams}')
            except Exception as ex:
                pass
        
        print('PESCADOS AZULES')
        for food in listaPescadoAzul:
            try:
                insertFoodCommand = Commands.InsertFoodCommand
                insertFoodCommand.FoodName = food.NameSpanish
                insertFoodCommand.FoodID = None
                insertFoodCommand.FoodDescription = food.DescriptionSpanish
                insertFoodCommand.FoodTypeID = 8
                tmpFood = Food.Create(Food,insertFoodCommand)
                if not self.foodRepository.ExistsByName(tmpFood.NombreIngrediente):
                    self.foodRepository.session.add(tmpFood)
                    self.foodRepository.session.commit()
                print(f'{food.NameSpanish} - {food.SaturatedFattyAcids.NameSpanish} - {food.SaturatedFattyAcids.GroupSpanish} - {food.SaturatedFattyAcids.EveryOneHundredGrams}')
            except Exception as ex:
                pass