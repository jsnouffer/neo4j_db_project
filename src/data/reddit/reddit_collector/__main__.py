import logging
import os
import sys

from praw import Reddit
from reddit_collector.redis import InputQueue

from neo4j import GraphDatabase

from reddit_collector import RedditNetwork, Comments
from reddit_collector.data_models import Redditor

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
        "bolt://localhost:7687", auth=("neo4j", "bitnami")
    )

    net = RedditNetwork(
        driver=driver,
        components=[
            # Other relationship types are Submissions and CommentsReplies
            # Other data models available as components are Subreddit and Submission
            Comments(Redditor(reddit, "BloodMooseSquirrel", limit=5)),
            Comments(Redditor(reddit, "Anub_Rekhan", limit=5))
        ]
    )
    # net.create_constraints()
    net.run_cypher_code()
    # net.add_karma(reddit)

    # queue = InputQueue()

    # sr = reddit.subreddit('all')
    # for comment in sr.stream.comments():
    #     queue.comment_queue.enqueue('reddit_collector.db.insert_comment', comment)
    #     queue.redditor_queue.enqueue('reddit_collector.db.insert_redditor', comment.author)
    #     queue.submission_queue.enqueue('reddit_collector.db.insert_submission', comment.submission)
    #     queue.subreddit_queue.enqueue('reddit_collector.db.insert_subreddit', comment.submission.subreddit)

if __name__ == "__main__":
    sys.exit(main()) 