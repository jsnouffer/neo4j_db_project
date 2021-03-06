import logging

from redis import Redis
from rq import Queue

logger = logging.getLogger(__name__)

class InputQueue():

    def __init__(self):

        logger.debug("connecting to Redis")
        self.redis = Redis(host='127.0.0.1')

        logger.debug("setting up Redis queues")
        self.redditor_queue = Queue('redditors', connection=self.redis)
        self.subreddit_queue = Queue('subreddits', connection=self.redis)
        self.submission_queue = Queue('submissions', connection=self.redis)
        self.comment_queue = Queue('comments', connection=self.redis)
        logger.info("done setting up Redis queues")
