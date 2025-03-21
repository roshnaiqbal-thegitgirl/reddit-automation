import logging
from auth import RedditAuthenticator
from fetch import RedditPostFetcher

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

def main():
    """Authenticates with Reddit and fetches the latest posts from a subreddit."""
    try:
        # Authenticate with Reddit
        authenticator = RedditAuthenticator()
        reddit_instance = authenticator.get_instance()

        # Define subreddit and post limit
        subreddit_name = "Python"
        post_limit = 5

        # Fetch latest posts
        fetcher = RedditPostFetcher(subreddit_name, post_limit)
        posts = fetcher.fetch_with_rate_limit_handling()

        # Display the retrieved posts
        if posts:
            logging.info(f"Latest {post_limit} posts from r/{subreddit_name}:")
            for idx, post in enumerate(posts, 1):
                logging.info(f"{idx}. {post['title']} (by {post['author']}) - Upvotes: {post['upvotes']}")
        else:
            logging.warning(f"No posts retrieved from r/{subreddit_name}.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
