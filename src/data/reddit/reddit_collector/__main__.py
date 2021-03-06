import logging
import os
import sys

from praw import Reddit
from reddit_collector.redis import InputQueue

def main():
    logger = logging.getLogger("main")
    logger.debug(os.environ.values())
    logger.debug("----------------------------------------------")

    logger.debug("connecting to Reddit")
    reddit = Reddit(client_id='Cz8OU1vxajnWDw',
        client_secret='5qax29ZPI2_Rdjc1TsXXEypFduk',
        user_agent='my user agent')
    logger.info("connected to Reddit")

    queue = InputQueue()

    sr = reddit.subreddit('all')
    for comment in sr.stream.comments():
        print(dir(comment))
        break
        # queue.comment_queue.enqueue('reddit_collector.db.insert_comment', comment)
        # queue.redditor_queue.enqueue('reddit_collector.db.insert_redditor', comment.author)
        # queue.submission_queue.enqueue('reddit_collector.db.insert_submission', comment.submission)
        # queue.subreddit_queue.enqueue('reddit_collector.db.insert_subreddit', comment.submission.subreddit)

if __name__ == "__main__":
    sys.exit(main()) 