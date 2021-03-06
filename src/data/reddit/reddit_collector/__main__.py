import logging
import os
import praw

from reddit_collector.GlobalContext import GlobalContext

if __name__ == "__main__":
    logger = logging.getLogger("main")
    logger.debug(os.environ.values())
    logger.debug("----------------------------------------------")

    ctx = GlobalContext()

    sr = ctx.Reddit.subreddit('all')

    for comment in sr.stream.comments():
        ctx.comment_queue.enqueue('reddit_collector.db.insert_comment', comment)
        ctx.redditor_queue.enqueue('reddit_collector.db.insert_redditor', comment.author)
        ctx.submission_queue.enqueue('reddit_collector.db.insert_submission', comment.submission)
        ctx.subreddit_queue.enqueue('reddit_collector.db.insert_subreddit', comment.submission.subreddit)

    
    # reddit = praw.Reddit(client_id='Cz8OU1vxajnWDw',
    #     client_secret='5qax29ZPI2_Rdjc1TsXXEypFduk',
    #     redirect_uri='http://localhost:8080',
    #     user_agent='my user agent')

    # print(reddit.auth.url(['identity'], '...', 'permanent'))

    # # assume you have a Reddit instance bound to variable `reddit`
    # subreddit = reddit.subreddit('minecraft')

    # print(subreddit.display_name)  # Output: redditdev
    # print(subreddit.title)         # Output: reddit Development
    # print(subreddit.description)   # Output: A subreddit for discussion of ...

    # for submission in subreddit.hot(limit=10):
    #     print(submission.title)  # Output: the submission's title
    #     print(submission.score)  # Output: the submission's score
    #     print(submission.id)     # Output: the submission's ID
    #     print(submission.url)    # Output: the URL the submission points to
    #                             # or the submission's URL if it's a self post