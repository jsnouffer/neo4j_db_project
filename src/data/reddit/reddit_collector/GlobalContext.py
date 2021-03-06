import os

from neomodel import config as neomodel_conf
from praw import Reddit
from redis import Redis
from rq import Queue


def test():
    return None

class Singleton:

    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

class GlobalContext(Singleton):

    def __init__(self):

        self.verbose = os.getenv("PLAYGROUND_VERBOSE") == "TRUE"

        #Instantiate the Reddit client
        if self.verbose:
            print(f"Connecting to Reddit")
        self.Reddit = Reddit(client_id='Cz8OU1vxajnWDw',
            client_secret='5qax29ZPI2_Rdjc1TsXXEypFduk',
            redirect_uri='http://localhost:8080',
            user_agent='my user agent')

        if self.verbose:
            print(f"Connected as: {self.Reddit.user.me()}")

        #Create database engine
        neomodel_conf.DATABASE_URL = 'bolt://neo4j:bitnami@localhost:7687'  #this connection method is a shame and i know it
        if self.verbose:
            print(f"Connected to Neo4j DB")

        # Connect to redis
        if self.verbose:
            print(f"Connecting to redis")
        self.redis = Redis(host='127.0.0.1')


        print(f"Setting up redis queues")
        self.test_queue = Queue('test', connection=self.redis)
        self.redditor_queue = Queue('redditors', connection=self.redis)
        self.subreddit_queue = Queue('subreddits', connection=self.redis)
        self.submission_queue = Queue('submissions', connection=self.redis)
        self.comment_queue = Queue('comments', connection=self.redis)
        print(f"Done setting up redis queues")
