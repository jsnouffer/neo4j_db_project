#!python
# cloned from https://neo4j.com/developer/python/
from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config

config.DATABASE_URL = "bolt://neo4j:bitnami@localhost:17687"

class Book(StructuredNode):
    title = StringProperty(unique_index=True)
    author = RelationshipTo('Author', 'AUTHOR')

class Author(StructuredNode):
    name = StringProperty(unique_index=True)
    books = RelationshipFrom('Book', 'AUTHOR')

if __name__ == "__main__":
    harry_potter = Book(title='Harry potter and the..').save()
    rowling =  Author(name='J. K. Rowling').save()
    harry_potter.author.connect(rowling)
