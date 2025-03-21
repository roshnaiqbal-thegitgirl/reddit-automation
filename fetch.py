import time
import logging
import praw
from prawcore.exceptions import RequestException, ResponseException, RateLimitExceeded
from auth import authenticate

class RedditPostFetcher:
    """Fetches the latest posts from a specified subreddit using the Reddit API."""

    def __init__(self, subreddit_name: str, post_limit: int = 5):
        self.reddit = authenticate()
        if not self.reddit:
            raise ConnectionError("Reddit authentication failed. Exiting...")

        self.subreddit_name = subreddit_name
        self.post_limit = post_limit

    def fetch_latest_posts(self):
        """
        Retrieves the latest posts from the specified subreddit.
        Includes rate limit handling.
        """
        try:
            subreddit = self.reddit.subreddit(self.subreddit_name)
            posts = subreddit.new(limit=self.post_limit)

            post_list = []
            for post in posts:
                post_data = {
                    "title": post.title,
                    "author": post.author.name if post.author else "Unknown",
                    "upvotes": post.score,
                }
                post_list.append(post_data)

            return post_list

        except RateLimitExceeded as e:
            logging.warning(f"Rate limit exceeded. Waiting for {e.sleep_time} seconds.")
            time.sleep(e.sleep_time)
            return self.fetch_latest_posts()

        except (RequestException, ResponseException) as e:
            logging.error(f"API request error: {e}")
            return []

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return []
