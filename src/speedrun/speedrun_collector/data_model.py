#from praw.models import Comment, reddit
from neomodel import Relationship, RelationshipFrom, RelationshipTo, StringProperty, StructuredNode
from neomodel.exceptions import DoesNotExist

#config.DATABASE_URL = 'bolt://neo4j:bitnami@localhost:8687'

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
    game_id = StringProperty(unique_index=True)
    user = RelationshipFrom('User', 'PLAYS')

    @classmethod
    def add(cls, name : str) -> 'Game':

        node: Game = cls.get(name)
        if node:
            return node
        return Game(game_id = name).save()

class User(SpeedrunNode):
    user_id = StringProperty(unique_index=True)
    games = RelationshipTo('Game', 'PLAYS')

    @classmethod
    def add(cls, title : str) -> 'User':

        node: User = cls.get(title)
        if node:
            return node
        return User(user_id = title).save()





