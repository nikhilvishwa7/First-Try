import re
import os
from os import environ
from pyrogram import enums
from Script import script

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['23640300'])
API_HASH = environ['b43066e201bfc457ad566e623fd74dab']
BOT_TOKEN = environ['6182908639:AAHL2qkqnlGzo0sNqXCsVIR5KmMX1kB4b2I']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/14ea49625341fb27b4df6.jpg')).split()
NOR_IMG = environ.get('NOR_IMG', "https://telegra.ph/file/356650716aeb2344fa985.jpg")
SPELL_IMG = environ.get('SPELL_IMG',"https://telegra.ph/file/3675ce6c5f511cc867ec7.jpg")

# Welcome area
MELCOW_IMG = environ.get('MELCOW_IMG',"https://telegra.ph/file/25c2ee07b3638d2005658.jpg")
MELCOW_VID = environ.get('MELCOW_VID',"https://telegra.ph/file/b04dd068fc8e2c2235f8d.mp4")



# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5149183428').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://nk3442838:nk3442838@cluster0.edymsnw.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Elsa")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = os.environ.get('MONGO_URL', "mongodb+srv://nk3442838:nk3442838@cluster0.edymsnw.mongodb.net/?retryWrites=true&w=majority")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

LANGUAGES = ["malayalam", "tamil", "english", "hindi", "telugu", "kannada"]

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
PORT = os.environ.get("PORT", "8080")
MAX_BTN = int(environ.get('MAX_BTN', "7"))
S_GROUP = environ.get('S_GROUP',"https://t.me/Newmovie_1st_on_tg")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/VisionBackup")
FILE_FORWARD = environ.get('FILE_FORWARD',"https://t.me/+FxDjIwqvtG4wMGNl")
MSG_ALRT = environ.get('MSG_ALRT', '𝗣𝗿𝗲𝘀𝗵𝗮𝗻 𝗠𝗮𝘁 𝗞𝗿 𝗕𝗰')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Filmy_Rog')
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE","<b>Your Query: {query}</b> \n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> |•| 10 \n\n💛 Please Share Us 💛\n\n‌‌‌‌Powered by: @FILMY_MEN")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


#Verify Features
VERIFY = bool(environ.get('VERIFY', True))
HOW_TO_VERIFY = environ.get("HOW_TO_VERIFY", "https://t.me/howtodownnload/11")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'mdisklink.link')
SHORTLINK_API = environ.get('SHORTLINK_API', '75e830d6e6bb44e5a2d13c1754ba7487f03a3336')
