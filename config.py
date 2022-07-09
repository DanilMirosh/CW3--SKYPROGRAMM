import os

JSON_AS_ASCII = False
TESTING = True
DEBUG = True
DATA_PATH_POSTS = os.path.join("data", "posts.json")
DATA_PATH_COMMENTS = os.path.join("data", "comments.json")
DATA_PATH_BOOKMARKS = os.path.join("data", "bookmarks.json")

LOGGER_API_PATH = os.path.join("logs", "api.logs")
LOGGER_FORMAT = f"%(asctime)s - [%(levelname)s] - %(message)s"
