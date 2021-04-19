from neomodel import Relationship, RelationshipFrom, RelationshipTo, StringProperty, StructuredNode
from neomodel.exceptions import DoesNotExist
from html import unescape

class HnNode(StructuredNode):
    __abstract_node__ = True

    @classmethod
    def get(cls, id: str) -> 'HnNode':

        kwargs: dict = {}
        kwargs[cls.__name__.lower() + "_id"] = id
        try:
            return cls.nodes.get(**kwargs)
        except DoesNotExist:
            return None

class Story(HnNode):
    story_id = StringProperty(unique_index=True)
    title = StringProperty()
    url = StringProperty()
    comments = RelationshipTo('Comment', 'ON')
    author = RelationshipTo('Author', 'BY')

    @classmethod
    def add(cls, story: dict) -> 'Story':
        node: Story = cls.get(story['id'])
        if node:
            return node
        return Story(story_id=story['id'], 
            title=unescape(story['title']),
            url=unescape(['url'])).save()

class Comment(HnNode):
    comment_id = StringProperty(unique_index=True)
    text = StringProperty()
    parent_story = RelationshipFrom('Story', 'ON')
    parent_comment = RelationshipFrom('Comment', 'ON')
    comments = RelationshipTo('Comment', 'ON')
    author = RelationshipTo('Author', 'BY')

    @classmethod
    def add(cls, comment: dict) -> 'Comment':
        node: Comment = cls.get(comment['id'])
        if node:
            return node
        return Comment(comment_id=comment['id'],
            text=unescape(comment['text'])).save()

    def add_connection(self, parent_node: HnNode) -> 'Comment':
        if type(parent_node) is Story:
            parent_node.comments.connect(self)
            return self
        elif type (parent_node) is Comment:
            parent_node.comments.connect(self)
            return self
        else:
            raise(ValueError("parent_node invalid type: " + str(type(parent_node))))
        return None

class Author(HnNode):
    author_id = StringProperty(unique_index=True)
    name = StringProperty()
    stories = RelationshipFrom('Story', 'BY')
    comments = RelationshipFrom('Comment', 'BY')

    @classmethod
    def add(cls, hn_node: dict) -> 'Author':
        node: Author = cls.get(hn_node['by'])
        if node:
            return node
        return Author(author_id=hn_node['by'], 
            name=unescape(hn_node['by'])).save()

    def add_connection(self, target_node: HnNode) -> 'Author':
        if type(target_node) is Story:
            target_node.author.connect(self)
            return self
        elif type (target_node) is Comment:
            target_node.author.connect(self)
            return self
        else:
            raise(ValueError("target_node invalid type: " + str(type(target_node))))
        return None
