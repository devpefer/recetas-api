from src.Application.Carbohydrates.Queries.queryhandler import CarbohydratesQueryHandler
from src.Application.Carbohydrates.Commands.commandhandler import CommandHandler
from src.Application.CarbohydrateTypes.Queries.queryhandler import QueryHandler
from src.Application.CarbohydrateTypes.Commands.commandhandler import CommandHandler
from src.Application.Fats.Queries.queryhandler import QueryHandler
from src.Application.Fats.Commands.commandhandler import CommandHandler
from src.Application.FatSubtypes.Queries.queryhandler import QueryHandler
from src.Application.FatSubtypes.Commands.commandhandler import CommandHandler
from src.Application.FatTypes.Queries.queryhandler import QueryHandler
from src.Application.FatTypes.Commands.commandhandler import CommandHandler
from src.Application.Minerals.Queries.queryhandler import QueryHandler
from src.Application.Minerals.Commands.commandhandler import CommandHandler
from src.Application.Relationship_Food_Carbohydrates.Queries.queryhandler import QueryHandler
from src.Application.Relationship_Food_Carbohydrates.Commands.commandhandler import CommandHandler
from src.Application.Relationship_Food_Vitamins.Queries.queryhandler import QueryHandler
from src.Application.Relationship_Food_Vitamins.Commands.commandhandler import CommandHandler
from src.Application.Vitamins.Queries.queryhandler import QueryHandler
from src.Application.Vitamins.Commands.commandhandler import CommandHandler
from mediatr import Mediator
import json

class RequestHandler():
    
    def __init__(self):
        self.mediatR = Mediator()
    
    def HandleQuery(self,request: object) -> object:
        response = self.mediatR.send(request)
        resultJson = json.dumps(response, cls=CustomJSONEncoder)
        return json.loads(resultJson)
        
    def HandleCommand(self,request: object):
        self.mediatR.send(request)
    
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
        