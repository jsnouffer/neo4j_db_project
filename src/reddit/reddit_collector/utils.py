from neomodel import config as neomodel_conf
from praw.models import Comment, MoreComments, reddit
from praw.models.comment_forest import CommentForest
from reddit_collector.data_model import Redditor, Subreddit
from reddit_collector.redis import InputQueue
from typing import List


USE_QUEUE: bool = True
NEO4J_URL: str = "bolt://neo4j:bitnami@localhost:7687"
queue = InputQueue()

def add_relationships(submission: reddit.submission.Submission) -> None:
    subreddit: Subreddit = Subreddit.add(submission.subreddit)
    redditor: Redditor = Redditor.add(submission.author)
    subreddit.submitter.connect(redditor)

    queue_comments(subreddit, redditor, submission.comments.list())

def queue_comments(subreddit: Subreddit, redditor: Redditor, comments: List["Comment"]):
    if len(comments) > 0:
        if USE_QUEUE:
            queue.comment_queue.enqueue('reddit_collector.utils.add_comments', subreddit, redditor, comments)
        else:
            add_comments(subreddit, redditor, comments)

def add_comments(subreddit: Subreddit, redditor: Redditor, comments: List["Comment"]):
    neomodel_conf.DATABASE_URL = NEO4J_URL
    for comment in comments:
        if isinstance(comment, MoreComments):
            if isinstance(comment.comments(), CommentForest):
                queue_comments(subreddit, redditor, comment.comments().list())
            else:
                queue_comments(subreddit, redditor, comment.comments())
        else:
            commenter: Redditor = redditor.addCollaborator(comment)
            if commenter is not None:
                subreddit.submitter.connect(commenter)
                queue_comments(subreddit, commenter, comment.replies.list())
            else:
                queue_comments(subreddit, redditor, comment.replies.list())
