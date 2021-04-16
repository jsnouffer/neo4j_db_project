import logging
import os
import sys


from neo4j import GraphDatabase


def main():
    logger = logging.getLogger("main")
    logger.debug(os.environ.values())
    logger.debug("----------------------------------------------")

    logger.debug("connecting to Reddit")
    reddit = Reddit(client_id='Cz8OU1vxajnWDw',
        client_secret='5qax29ZPI2_Rdjc1TsXXEypFduk',
        user_agent='my user agent')
    logger.info("connected to Reddit")

    # Create driver instance
    driver = GraphDatabase.driver(
        "bolt://localhost:17687", auth=("neo4j", "bitnami")
    )


if __name__ == "__main__":
    sys.exit(main()) 