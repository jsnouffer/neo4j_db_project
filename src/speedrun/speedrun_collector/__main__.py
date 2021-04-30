import logging
import os
import sys

from neomodel import config

def main():
    logger = logging.getLogger("main")
    logger.debug(os.environ.values())
    logger.debug("----------------------------------------------")

    config.DATABASE_URL = 'bolt://neo4j:bitnami@localhost:7687'

if __name__ == "__main__":
    sys.exit(main()) 