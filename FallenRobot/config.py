class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "22428981"
    API_HASH = "e1eb486688d13fda52ad6afb934e3a34"

    CASH_API_KEY = "IO4NXBOQG98MA9XT"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "dnlqgqfn:***@snuffleupagus.db.elephantsql.com/dnlqgqfn"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001889732247)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Bikash:Bikashop@bikash.cbkkx4c.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/78367765adad0251c0481.jpg"

    SUPPORT_CHAT = "https://t.me/harmonie_43"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6350868350:AAFWFHiHxB8131IQwRgPdPpIL_UeLxCiI-s"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "KVGXY2V5BLQC"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5901986773  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
