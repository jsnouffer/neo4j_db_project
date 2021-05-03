from praw.models import Comment, reddit

from neomodel import Relationship, RelationshipFrom, RelationshipTo, StringProperty, StructuredNode
from neomodel.exceptions import DoesNotExist


class RedditNode(StructuredNode):
    __abstract_node__ = True

    @classmethod
    def get(cls, id: str) -> 'RedditNode':

        kwargs: dict = {}
        kwargs[cls.__name__.lower() + "_id"] = id
        try:
            return cls.nodes.get(**kwargs)
        except DoesNotExist:
            return None

class Subreddit(RedditNode):
    subreddit_id = StringProperty(unique_index=True)
    name = StringProperty()
    submission = RelationshipFrom('Submission', 'SUBMISSION')

    @classmethod
    def add(cls, subreddit: reddit.subreddit.Subreddit) -> 'Subreddit':

        node: Subreddit = cls.get(subreddit.id)
        if node:
            return node
        return Subreddit(subreddit_id=subreddit.id, name=str(subreddit)).save()

class Submission(RedditNode):
    submission_id = StringProperty(unique_index=True)
    text = StringProperty()
    submitter = RelationshipFrom('Redditor', 'SUBMITTER')

    @classmethod
    def add(cls, submission: reddit.submission.Submission) -> 'Submission':

        node: Submission = cls.get(submission.id)
        if node:
            return node
        return Submission(submission_id=submission.id, text=str(submission)).save()

class Redditor(RedditNode):
    redditor_id = StringProperty(unique_index=True)
    submitter = RelationshipTo('Submission', 'SUBMITTER')
    collaborator = Relationship('Redditor', 'INTERACTED')
    redditor: reddit.redditor.Redditor = None

    @classmethod
    def add(cls, redditor: reddit.redditor.Redditor) -> 'Redditor':

        node: Redditor = cls.get(redditor.name)
        if node:
            return node
        return Redditor(redditor_id=redditor.name).save()

    def addCollaborator(self, comment: Comment) -> 'Redditor':
        if comment.author is None:
            return None

        node: Redditor = Redditor.add(comment.author)
        if node.redditor_id != self.redditor_id:
            node.collaborator.connect(self)
            return node

        return None
