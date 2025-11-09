import praw
import csv

# Setup Reddit API credentials
reddit = praw.Reddit(
    client_id="id",
    client_secret="secret",
    user_agent="top1k-1000-posts",
)

# Get the top 1,000 posts from the subreddit
top_posts = reddit.subreddit("Entrepreneur").top(limit=1000)

# Open a CSV file to write the data
with open("top_1000.csv", "w", newline="") as csvfile:
    fieldnames = ["title", "score", "num_comments", "author"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for post in top_posts:
        writer.writerow(
            {
                "title": post.title,
                "score": post.score,
                "num_comments": post.num_comments,
                "author": str(post.author),
            }
        )
