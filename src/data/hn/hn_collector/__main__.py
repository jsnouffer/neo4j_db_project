from collections import defaultdict
import logging
import os
import sys
import json
import requests

from neo4j import GraphDatabase
from neomodel import config as neomodel_conf
from data_model import *

NEO4J_URL: str = "bolt://neo4j:bitnami@localhost:17687"

def get_stories(topic: str) -> dict:
    url = 'https://hn.algolia.com/api/v1/search?query=topic'.format(topic)
    response = requests.get(url)
    results: dict = response.json()
    return results

def ingest_story(node_id: str) -> dict:
    url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(node_id)
    response = requests.get(url)
    results: dict = response.json()
    story = Story.add(results)
    author = Author.add(results)
    author.add_connection(story)
    return results

def main():
    neomodel_conf.DATABASE_URL = NEO4J_URL
    stories = get_stories('minecraft')
    for story in stories['hits']:
        print('story ' + story['objectID'] + ' by ' + story['author'])
        ingest_story(story['objectID'])
        break

if __name__ == "__main__":
    sys.exit(main()) 

# ## neo4j
# class HelloWorldExample:

#     def __init__(self, driver):
#         self.driver = driver

#     def print_greeting(self, message):
#         with self.driver.session() as session:
#             greeting = session.write_transaction(self._create_and_return_greeting, message)
#             print(greeting)

#     @staticmethod
#     def _create_and_return_greeting(tx, message):
#         result = tx.run("CREATE (a:Greeting) "
#                         "SET a.message = $message "
#                         "RETURN a.message + ', from node ' + id(a)", message=message)
#         return result.single()[0]

# # neomodel
# class Book(StructuredNode):
#     title = StringProperty(unique_index=True)
#     author = RelationshipTo('Author', 'AUTHOR')

# class Author(StructuredNode):
#     name = StringProperty(unique_index=True)
#     books = RelationshipFrom('Book', 'AUTHOR')


# def main():
#     print("hello")
#     print(os.environ.values())
#     print("----------------------------------------------")

#     print("connecting to hn")

#     # Create driver instance
#     print("connecting to neo4j")
#     driver = GraphDatabase.driver(
#         "bolt://localhost:17687", auth=("neo4j", "bitnami")
#     )
#     print("writing hello message")
#     greeter = HelloWorldExample(driver)
#     greeter.print_greeting('hello neo4j')
#     driver.close()

#     print("closed to neo4j")

#     print("using neomodel")
#     config.DATABASE_URL = 'bolt://neo4j:bitnami@localhost:17687'
#     print("adding Harry Potter")

#     harry_potter = Book(title='Harry potter and the..').save()
#     rowling =  Author(name='J. K. Rowling').save()
#     harry_potter.author.connect(rowling)

#     print("added Harry Potter")

# if __name__ == "__main__":
#     sys.exit(main()) 