import datetime

from neomodel import config as neomodel_conf
from neomodel import (StructuredNode, StringProperty, IntegerProperty, BooleanProperty, RelationshipTo, One, DateTimeProperty)
from praw import models as praw_models

NEO4J_URL: str = "bolt://neo4j:bitnami@localhost:7687"

class Redditor(StructuredNode):
    rid = StringProperty(unique_index=True)
    name = StringProperty(index=True)
    comment_karma = IntegerProperty()
    link_karma = IntegerProperty()
    is_employee = BooleanProperty()
    is_mod = BooleanProperty()
    is_gold = BooleanProperty()
    created_utc = DateTimeProperty(index=True)


class Subreddit(StructuredNode):

    # Labels
    rid = StringProperty(unique_index=True)
    name = StringProperty(index=True)
    display_name = StringProperty(index=True)
    description = StringProperty()
    num_subscribers = IntegerProperty()
    is_nsfw = BooleanProperty(index=True)
    created_utc = DateTimeProperty(index=True)

    # Edges
    submitters = RelationshipTo('reddit_collector.db.Redditor', 'SUBMITTED')
    subcribers = RelationshipTo('reddit_collector.db.Redditor', 'IS_SUBSCRIBED')
    moderators = RelationshipTo('reddit_collector.db.Redditor', 'MODERATES')


class Submission(StructuredNode):
    pass


class Comment(StructuredNode):

    # Labels
    rid = StringProperty(unique_index=True)
    body = StringProperty()
    score = IntegerProperty()
    stickied = BooleanProperty()
    permalink = StringProperty(index=True)
    created_utc = DateTimeProperty(index=True)

    # Edges
    author = RelationshipTo('reddit_collector.db.Redditor', 'COMMENTED', cardinality=One)
    submission = RelationshipTo('reddit_collector.db.Submission', 'COMMENTED_ON', cardinality=One)
    parent_comment = RelationshipTo('reddit_collector.db.Comment', 'REPLIED_TO')


def insert_comment(comment: praw_models.Comment):
    neomodel_conf.DATABASE_URL = NEO4J_URL

    cmt = Comment(rid=comment.id,
                          body=comment.body,
                          score=comment.score,
                          stickied=comment.stickied,
                          permalink=comment.permalink,
                          created_utc=datetime.datetime.fromtimestamp(comment.created_utc)
                          ).save()

def insert_redditor(redditor: praw_models.Redditor):
    neomodel_conf.DATABASE_URL = NEO4J_URL

    rdt = Redditor(rid=redditor.id,
                   name=redditor.name,
                   comment_karma=redditor.comment_karma,
                   link_karma=redditor.link_karma,
                   is_employee=redditor.is_employee,
                   is_mod=redditor.is_mod,
                   is_gold=redditor.is_gold,
                   created_utc=datetime.datetime.fromtimestamp(redditor.created_utc)
                   ).save()


def insert_submission(submission: praw_models.Submission):
    neomodel_conf.DATABASE_URL = NEO4J_URL

def insert_subreddit(subreddit: praw_models.Subreddit):
    neomodel_conf.DATABASE_URL = NEO4J_URL

    srt = Subreddit(rid=subreddit.id,
                    name=subreddit.name,
                    display_name=subreddit.display_name,
                    description=subreddit.public_description,
                    num_subscribers=subreddit.subscribers,
                    is_nsfw=subreddit.over18,
                    created_utc=datetime.datetime.fromtimestamp(subreddit.created_utc)
                    ).save()
