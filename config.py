import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("25136173"))
API_HASH = getenv("bc54f0b258c285687840966937035aa0")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("5893596243:AAHs8y6LPdkebW1qSfMsqUhmbuqr2QD44lc")

#Get API_KEY from @DeadlineTechOwner or @DeadlineApiBot
API_BASE_URL = getenv("API_BASE_URL", "https://deadlinetech.site")
API_KEY = getenv("API_KEY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1001575489651", None))

# Get this value from @Harry_RoxBot on Telegram by /id
OWNER_ID = int(getenv("974227248", 6848223695))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://t.me/+u4YKT_x5nZUwMDc9",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Words_by_heart0")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+NDcbNyONoVQ5NzNl")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQF_jC0AMGnQHNY0_XWiSGjNmteX9FWzD61r2KwaeUsw4rn9ydoqHS2UrWqJQfcRqw-gC1BialX1ro9ohPlPY8VlOXBkXDp__3cQuDCc8fB_lHaCNSY_LQ1eGKpKbdpqPWQI-wiauA8HtkAmdkpfGv930oaEwro9jxR5LOr9QBIW6iYSdUZFVkbQYZy-7i-V48_d3CMmGCBCpRD8fMe1ZNM0ujlokh76DsswoIdP8ctvWuE0qrD8FdaYQnJIRFrc8b4UajXW__dtAhcnQx8kqd5VtPDNx8aeyFQuag8grkMeUWk8ioBrXmmVqMUrIe1pMYyjZFzwhK7sEoB79cxezOfUzmki5gAAAAHV0F1jAA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/pjwlqg.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/ou29gb.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/tny9ug.jpg"
STATS_IMG_URL = "https://files.catbox.moe/k3e3bg.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/nknnw1.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/1xn73k.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/tny9ug.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/1xn73k.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/fpknxj.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/1xn73k.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/1xn73k.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/1xn73k.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
