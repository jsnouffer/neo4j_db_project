import logging
import os
import sys

from neomodel import Relationship, RelationshipFrom, RelationshipTo, StringProperty, StructuredNode
from neomodel.exceptions import DoesNotExist

#try:
    #FOR REGULAR MAKE
from speedrun_collector.speedrunScraper import *
#except:
    #FOR DEBUGGING
#    from speedrunScraper import *

from neomodel import config

def main():
    logger = logging.getLogger("main")
    logger.debug(os.environ.values())
    logger.debug("----------------------------------------------")

    config.DATABASE_URL = 'bolt://neo4j:bitnami@localhost:8687'

    user_scraper()

    #class Game(StructuredNode):
    #    title = StringProperty(unique_index=True)
    #    user = RelationshipTo('User', 'USER')

    #class User(StructuredNode):
    #    name = StringProperty(unique_index=True)
    #    games = RelationshipFrom('Game', 'USER')

    #first_game = Game(title='Minecraft').save()
    #first_user = User(name='Cactus').save()
    #first_game.user.connect(first_user)

    first_game = Game(title='Minecraft').save()

if __name__ == "__main__":
    sys.exit(main()) 