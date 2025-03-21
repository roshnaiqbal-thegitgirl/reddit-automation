import logging
from auth import RedditAuthenticator
from fetch_posts import RedditPostFetcher

# Handles logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

def main():
    """Main execution function to authenticate and fetch subreddit posts."""
    logging.info("Starting Reddit automation script...")

    # Authenticate with Reddit
    try:
        authenticator = RedditAuthenticator()
        reddit_instance = authenticator.get_instance()
    except Exception as e:
        logging.critical("Failed to authenticate. Exiting program.")
        exit(1)

    # Fetch latest posts from a subreddit
    subreddit_name = "learnpython"  # Change to your target subreddit
    post_fetcher = RedditPostFetcher(reddit_instance, subreddit_name, post_limit=5)

    try:
        posts = post_fetcher.fetch_latest_posts()
        if posts:
            logging.info(f"Displaying {len(posts)} latest posts from r/{subreddit_name}:\n")
            for i, post in enumerate(posts, start=1):
                print(f"{i}. Title: {post['title']}\n   Author: {post['author']}\n   Upvotes: {post['upvotes']}\n")
        else:
            logging.warning("No posts retrieved. Check the subreddit name or API response.")
    
    except Exception as e:
        logging.error(f"Error fetching posts: {e}")
    
    logging.info("Reddit automation script completed.")

if __name__ == "__main__":
    main()
