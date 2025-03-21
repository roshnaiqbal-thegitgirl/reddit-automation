# Reddit Automation using Python

## Description
This project automates interactions with Reddit using the **Reddit API (PRAW)**. It enables authentication via OAuth and retrieves the latest posts from a specified subreddit. The project follows best practices, including handling API rate limits and securely storing credentials.

## Features
- **Authentication:** Securely connects to Reddit using OAuth.
- **Fetching Posts:** Retrieves and displays the latest subreddit posts with their titles, authors, and upvote counts.
- **Error Handling:** Manages authentication failures, API rate limits, and other exceptions.
- **Modular Code:** Organized structure with `auth.py`, `fetch_posts.py`, and `main.py`.
- **Secure Credentials:** Uses a `.env` file to store API keys securely.

## Project Structure
```
reddit-automation/
│── auth.py           # Handles Reddit API authentication  
│── fetch_posts.py    # Fetches latest posts from a subreddit  
│── main.py           # Runs the script  
│── .env              # Stores API credentials (not committed to Git)  
│── requirements.txt  # Lists dependencies  
│── README.md         # Project setup and usage guide  
│── .gitignore        # Excludes sensitive files from Git  
```

## Technologies Used
- **Python** (Primary language)
- **PRAW** (Python Reddit API Wrapper)
- **VS Code** (Development Environment)
- **Git & GitHub** (Version Control)
- **dotenv** (Secure API credential storage)

## Installation & Setup

### Clone the Repository
Choose **one** of the following methods:

- **Using HTTPS:**
  ```bash
  git clone https://github.com/roshnaiqbal-thegitgirl/reddit-automation.git
  ```
- **Using SSH:**
  ```bash
  git clone git@github.com:roshnaiqbal-thegitgirl/reddit-automation.git
  ```
  (Ensure SSH is set up on your GitHub account.)

```bash
cd reddit-automation
```

### Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt  
```

### Set Up API Credentials
- Create a `.env` file in the project root.
- Add the following credentials (replace with your values):
  ```
  CLIENT_ID=your_client_id
  CLIENT_SECRET=your_client_secret
  USERNAME=your_reddit_username
  PASSWORD=your_reddit_password
  USER_AGENT=your_app_name/1.0 by your_reddit_username
  ```
- **Important:** Never share your `.env` file or push it to GitHub.

## Running the Script
Once set up, run:
```bash
python main.py  
```

It will authenticate with Reddit and fetch the latest **5 posts** from the specified subreddit.

## License
This project is licensed under the **MIT License**.

## Contributing
Feel free to fork the repository, create a new branch, and submit a pull request for improvements.

