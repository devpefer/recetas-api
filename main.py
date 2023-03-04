import sys
from os import path
sys.path.append(path.dirname(path.dirname( path.abspath(__file__))))
from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from src.API.Controllers.CarbohydratesController.carbohydratescontroller import CarbohydratesController
from src.API.Controllers.CarbohydrateTypesController.carbohydratetypescontroller import CarbohydrateTypesController
from src.API.Controllers.FatsController.fatscontroller import FatsController
from src.API.Controllers.FatSubtypesController.fatsubtypescontroller import FatSubtypesController
from src.API.Controllers.FatTypesController.fattypescontroller import FatTypesController
from src.API.Controllers.FoodController.foodcontroller import FoodController
from src.API.Controllers.MineralsController.mineralscontroller import MineralsController
from src.API.Controllers.RelationshipFoodCarbohydrate.relationshipfoodcarbohydratecontroller import RelationshipFoodCarbohydrateController
from mediatr import Mediator

app = FastAPI()

app.include_router(CarbohydratesController.router)
app.include_router(CarbohydrateTypesController.router)
app.include_router(FatsController.router)
app.include_router(FatSubtypesController.router)
app.include_router(FatTypesController.router)
app.include_router(FoodController.router)
app.include_router(MineralsController.router)
app.include_router(RelationshipFoodCarbohydrateController.router)
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")