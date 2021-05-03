import logging
import os
import sys


from praw import Reddit

from neomodel import config
from reddit_collector.utils import *


def main():
    logger = logging.getLogger("main")
    logger.debug(os.environ.values())
    logger.debug("----------------------------------------------")

    logger.debug("connecting to Reddit")
    reddit = Reddit(client_id='Cz8OU1vxajnWDw',
        client_secret='5qax29ZPI2_Rdjc1TsXXEypFduk',
        user_agent='my user agent')
    logger.info("connected to Reddit")

    config.DATABASE_URL = 'bolt://neo4j:bitnami@localhost:7687'

    subreddit = reddit.subreddit("minecraft")
    for submission in subreddit.hot(limit=10):
        add_relationships(submission)


if __name__ == "__main__":
    sys.exit(main()) 