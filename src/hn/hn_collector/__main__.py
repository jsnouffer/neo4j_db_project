from collections import defaultdict
import logging
import os
import sys
import json
import requests

from neo4j import GraphDatabase
from neomodel import config as neomodel_conf
from .data_model import *

from dotenv import find_dotenv, load_dotenv

# delete all: MATCH (n) DETACH DELETE n

def get_stories(topic: str) -> dict:
    url = 'https://hn.algolia.com/api/v1/search?query={}&page={}'.format(topic,0)
    response = requests.get(url)
    results: dict = response.json()
    return results

def ingest_comment(parent: HnNode, node_id:str)-> dict:
    url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(node_id)
    response = requests.get(url)
    results: dict = response.json()
    if 'deleted' not in results:
        comment = Comment.add(results)
        author = Author.add(results)
        author.add_connection(comment)
        comment.add_connection(parent)
        if 'kids' in results:
            for kid in results['kids']:
                ingest_comment(comment, str(kid)) 
    return results

def ingest_story(node_id: str) -> dict:
    url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(node_id)
    response = requests.get(url)
    results: dict = response.json()
    story = Story.add(results)
    author = Author.add(results)
    author.add_connection(story)
    if 'kids' in results:
        for kid in results['kids']:
            ingest_comment(story, str(kid)) 
    return results

def main():
    load_dotenv(find_dotenv())
    logger = logging.getLogger("main")
    logger.debug(os.environ.values())
    logger.debug("----------------------------------------------")
    logger.debug("opening neomodel " + os.getenv('NEO4J_URL'))
    neomodel_conf.DATABASE_URL = os.getenv('NEO4J_URL')
    stories = get_stories('minecraft') # returns top 20 stories
    for story in stories['hits']:
        logger.info('ingesting story ' + story['objectID'] + ' by ' + story['author'])
        ingest_story(story['objectID'])

if __name__ == "__main__":
    sys.exit(main()) 
