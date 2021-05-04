#from praw.models import Comment, reddit
from neomodel import Relationship, RelationshipFrom, RelationshipTo, StringProperty, StructuredNode
from neomodel.exceptions import DoesNotExist

config.DATABASE_URL = 'bolt://neo4j:bitnami@localhost:8687'

class SpeedrunNode(StructuredNode):
    __abstract_node__ = True

    @classmethod
    def get(cls, id: str) -> 'SpeedrunNode':

        kwargs: dict = {}
        kwargs[cls.__name__.lower() + "_id"] = id
        try:
            return cls.nodes.get(**kwargs)
        except DoesNotExist:
            return None

class Game(SpeedrunNode):
    title = StringProperty(unique_index=True)
    user = RelationshipTo('User', 'USER')

class User(SpeedrunNode):
    name = StringProperty(unique_index=True)
    games = RelationshipFrom('Game', 'USER')

first_game = Game(title='Minecraft').save()
first_user = User(name='Cactus').save()
first_game.user.connect(first_user)




