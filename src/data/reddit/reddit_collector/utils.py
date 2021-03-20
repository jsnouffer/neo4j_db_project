from praw.models import Comment, MoreComments, reddit
from reddit_collector.data_model import Redditor, Subreddit
from typing import List

def add_relationships(submission: reddit.submission.Submission) -> None:
    subreddit: Subreddit = Subreddit.add(submission.subreddit)
    redditor: Redditor = Redditor.add(submission.author)
    subreddit.submitter.connect(redditor)

    add_comments(subreddit, redditor, submission.comments.list())

def add_comments(subreddit: Subreddit, redditor: Redditor, comments: List["Comment"]):
    for comment in comments:
        if isinstance(comment, MoreComments):
            add_comments(subreddit, redditor, comment.comments())
        else:
            commenter: Redditor = redditor.addCollaborator(comment)
            if commenter is not None:
                subreddit.submitter.connect(commenter)
                add_comments(subreddit, commenter, comment.replies.list())
            else:
                add_comments(subreddit, redditor, comment.replies.list())
