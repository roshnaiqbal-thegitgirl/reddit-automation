import os
import praw
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

class RedditAuthenticator:
    """Handles authentication with the Reddit API using PRAW."""

    def __init__(self):
        """Loads API credentials and initializes authentication."""
        self._load_credentials()
        self.reddit = self._authenticate()

    def _load_credentials(self):
        """Loads Reddit API credentials from the .env file."""
        load_dotenv()
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        self.username = os.getenv("REDDIT_USERNAME")
        self.password = os.getenv("REDDIT_PASSWORD")
        self.user_agent = os.getenv("REDDIT_USER_AGENT")

        # Validate credentials
        missing_credentials = [key for key, value in {
            "REDDIT_CLIENT_ID": self.client_id,
            "REDDIT_CLIENT_SECRET": self.client_secret,
            "REDDIT_USERNAME": self.username,
            "REDDIT_PASSWORD": self.password,
            "REDDIT_USER_AGENT": self.user_agent
        }.items() if not value]

        if missing_credentials:
            logging.error(f"Missing required API credentials: {', '.join(missing_credentials)}")
            raise ValueError("Reddit API credentials are not set properly. Check your .env file.")

    def _authenticate(self):
        """Authenticates with the Reddit API and returns a PRAW Reddit instance."""
        try:
            reddit_instance = praw.Reddit(
                client_id=self.client_id,
                client_secret=self.client_secret,
                username=self.username,
                password=self.password,
                user_agent=self.user_agent,
            )
            # Verify authentication
            authenticated_user = reddit_instance.user.me()
            logging.info(f"Successfully authenticated as: {authenticated_user}")
            return reddit_instance

        except Exception as error:
            logging.error(f"Authentication failed: {error}")
            raise

    def get_instance(self):
        """Returns the authenticated Reddit instance."""
        return self.reddit


# Standalone execution for testing authentication
if __name__ == "__main__":
    try:
        authenticator = RedditAuthenticator()
        reddit_instance = authenticator.get_instance()
        logging.info("🔹 Authentication test successful.")
    except Exception as e:
        logging.critical("Fatal error in authentication. Exiting.")
        exit(1)