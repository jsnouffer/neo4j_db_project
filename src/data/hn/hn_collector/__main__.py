import logging
import os
import sys

from neo4j import GraphDatabase
from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config

## neo4j
class HelloWorldExample:

    def __init__(self, driver):
        self.driver = driver

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

# neomodel
class Book(StructuredNode):
    title = StringProperty(unique_index=True)
    author = RelationshipTo('Author', 'AUTHOR')

class Author(StructuredNode):
    name = StringProperty(unique_index=True)
    books = RelationshipFrom('Book', 'AUTHOR')


def main():
    print("hello")
    print(os.environ.values())
    print("----------------------------------------------")

    print("connecting to hn")

    # Create driver instance
    print("connecting to neo4j")
    driver = GraphDatabase.driver(
        "bolt://localhost:17687", auth=("neo4j", "bitnami")
    )
    print("wrinting hello message")
    greeter = HelloWorldExample(driver)
    greeter.print_greeting('hello neo4j')
    driver.close()

    print("closed to neo4j")

    print("using neomodel")
    config.DATABASE_URL = 'bolt://neo4j:bitnami@localhost:17687'
    print("adding Harry Potter")

    harry_potter = Book(title='Harry potter and the..').save()
    rowling =  Author(name='J. K. Rowling').save()
    harry_potter.author.connect(rowling)

    print("added Harry Potter")

if __name__ == "__main__":
    sys.exit(main()) 