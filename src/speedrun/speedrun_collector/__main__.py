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

    get_user_games()

if __name__ == "__main__":
    sys.exit(main()) 