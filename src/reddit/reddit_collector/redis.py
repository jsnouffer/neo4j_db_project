import logging

from redis import Redis
from rq import Queue

logger = logging.getLogger(__name__)

class InputQueue():

    def __init__(self):

        logger.debug("connecting to Redis")
        self.redis = Redis(host='127.0.0.1')

        logger.debug("setting up Redis queues")
        self.comment_queue = Queue('comments', connection=self.redis)
        logger.info("done setting up Redis queues")