import time
import logging
from praw.exceptions import APIException, ClientException
from prawcore.exceptions import RequestException, ResponseException
from auth import RedditAuthenticator

class RedditPostFetcher:
    """Fetches the latest posts from a specified subreddit using the Reddit API."""

    def __init__(self, subreddit_name: str, post_limit: int = 5):
        self.reddit = RedditAuthenticator().get_instance()
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

        except RequestException as e:
            logging.error(f"Network error: {e}")
            return []

        except ResponseException as e:
            logging.error(f"API response error: {e}")
            return []

        except APIException as e:
            logging.error(f"Reddit API error: {e}")
            return []

        except ClientException as e:
            logging.error(f"PRAW client error: {e}")
            return []

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return []

    def fetch_with_rate_limit_handling(self):
        """Fetches posts while handling Reddit’s rate limits."""
        while True:
            try:
                return self.fetch_latest_posts()
            except APIException as e:
                if "RATELIMIT" in str(e).upper():
                    logging.warning("Rate limit exceeded. Sleeping for 60 seconds...")
                    time.sleep(60)
                else:
                    raise

# Standalone execution for testing post retrieval
if __name__ == "__main__":
    subreddit_name = "Python"
    fetcher = RedditPostFetcher(subreddit_name)
    posts = fetcher.fetch_with_rate_limit_handling()

    if posts:
        logging.info(f"Latest posts from r/{subreddit_name}:")
        for idx, post in enumerate(posts, 1):
            logging.info(f"{idx}. {post['title']} (by {post['author']}) - Upvotes: {post['upvotes']}")
    else:
        logging.warning(f"No posts retrieved from r/{subreddit_name}.")
