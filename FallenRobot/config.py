class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 22600695
    API_HASH = "23081df16fad795e9cf1ebeb6ffb94dd"

    CASH_API_KEY = "CNPMB8B1ONC6TRXG"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://ackyjued:cN4X7C8yfFcrCu6gUROrc5O92dkdkPht@satao.db.elephantsql.com/ackyjued"  # A sql database url from elephantsql.com

    EVENT_LOGS = "TheBotCollections"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://rmpatel977:<password>@cluster0.dmmssgr.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/85babd529df9d2e78a5cc.jpg"

    SUPPORT_CHAT = "TheBotSupportChat"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6798521059:AAEaB7f__QkvB0vRYGehYwlmT4N5Hha6kmo"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "I9A5CZST52I1"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6628968449  # User id of your telegram account (Must be integer)

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
