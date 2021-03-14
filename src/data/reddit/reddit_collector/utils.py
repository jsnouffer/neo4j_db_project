from praw.models import reddit
from reddit_collector.data_model import Redditor, Submission, Subreddit


ADD_SUBMISSION_NODES: bool = True

def add_relationships(submission: reddit.submission.Submission) -> None:

    if ADD_SUBMISSION_NODES:
        node: Submission = Submission.add(submission)
        node.subreddit.connect(Subreddit.add(submission.subreddit))
        node.author.connect(Redditor.add(submission.author))
    else:
        Subreddit.add(submission.subreddit).submitter.connect(Redditor.add(submission.author))