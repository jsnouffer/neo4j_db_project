import logging.config
import logging
import os
import yaml
from dotenv import load_dotenv

from reddit_collector.network import RedditNetwork
from reddit_collector.relationships import Comments, CommentsReplies, Submissions

load_dotenv(os.getenv('CONFIG_ENV'))

try:
    with open('logging.yaml', 'rt') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
    logging.config.dictConfig(config)
except FileNotFoundError:
    print("No valid logging file found")