from praw.models import reddit

from neomodel import StringProperty, RelationshipFrom, RelationshipTo, StructuredNode
from neomodel.exceptions import DoesNotExist


class RedditNode(StructuredNode):
    __abstract_node__ = True

    @classmethod
    def get(cls, id: str) -> 'Submission':

        kwargs: dict = {}
        kwargs[cls.__name__.lower() + "_id"] = id
        try:
            return cls.nodes.get(**kwargs)
        except DoesNotExist:
            return None


class Submission(RedditNode):
    submission_id = StringProperty(unique_index=True)
    subreddit = RelationshipTo('Subreddit', 'CHILD')
    author = RelationshipFrom('Redditor', 'AUTHOR')

    @classmethod
    def add(cls, submission: reddit.submission.Submission) -> 'Submission':
        uid: str = submission.subreddit_id + "_" + submission.id
        node: Submission = cls.get(uid)
        if not node:
            node = Submission(submission_id=uid).save()

        return node

class Subreddit(RedditNode):
    subreddit_id = StringProperty(unique_index=True)
    name = StringProperty()
    submission = RelationshipFrom('Submission', 'CHILD')
    submitter = RelationshipFrom('Redditor', 'SUBMITTER')

    @classmethod
    def add(cls, subreddit: reddit.subreddit.Subreddit) -> 'Subreddit':

        node: Subreddit = cls.get(subreddit.id)
        if node:
            return node
        return Subreddit(subreddit_id=subreddit.id, name=str(subreddit)).save()

class Redditor(RedditNode):
    redditor_id = StringProperty(unique_index=True)
    name = StringProperty()
    submission = RelationshipTo('Submission', 'AUTHOR')
    submitter = RelationshipFrom('Subreddit', 'SUBMITTER')

    @classmethod
    def add(cls, redditor: reddit.redditor.Redditor) -> 'Redditor':

        node: Redditor = cls.get(redditor.id)
        if node:
            return node
        return Redditor(redditor_id=redditor.id, name=redditor.name).save()