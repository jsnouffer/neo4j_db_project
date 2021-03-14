import logging
import os
import sys


from praw import Reddit
# from neo4j import GraphDatabase

# from reddit_detective import RedditNetwork, Comments, Submissions
# from reddit_detective.data_models import Subreddit

from neomodel import config
from reddit_collector.data_model import Submission, Subreddit
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

    # driver = GraphDatabase.driver(
    #     "bolt://localhost:7687", auth=("neo4j", "bitnami")
    # )

    config.DATABASE_URL = 'bolt://neo4j:bitnami@localhost:7687'

    subreddit = reddit.subreddit("minecraft")
    for submission in subreddit.hot(limit=5):
        add_relationships(submission)

        # print(dir(submission))


    # session = driver.session()
    # print(dir(session))

    # user = db.labels.create("User")

    # subreddit = reddit.subreddit("minecraft")
    # print(dir(subreddit))

    # for submission in subreddit.hot(limit=5):
    #     user.add(db.nodes.create(name=submission.author))
    #     # print(dir(submission))
        


    # network = RedditNetwork(
    #     driver=driver,
    #     components=[
    #         # Other relationship types are Submissions and CommentsReplies
    #         # Other data models available as components are Subreddit and Submission
    #         # Comments(Redditor(reddit, "BloodMooseSquirrel", limit=5)),
    #         # Comments(Redditor(reddit, "Anub_Rekhan", limit=5))
    #         Submissions(Subreddit(reddit, "doctorwho", limit=10))
    #     ]
    # )

    # try:
    #     network.create_constraints()
    # except:
    #     logger.info("Constraint already created")
    # network.run_cypher_code()

if __name__ == "__main__":
    sys.exit(main()) 