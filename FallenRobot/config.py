class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 20515794
    API_HASH = "da128bd223a333f5bde8dc1359db4609"

    CASH_API_KEY = "X7NAUI7VZAP5YSHD"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "fee800d5-9478-45ef-82da-3f6a93c38d4e"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002011859910)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://synaxxkhushi:synaxherebaby@cluster0.vqzfrg0.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/4935c97f373a278e04130.jpg"

    SUPPORT_CHAT = "synaxchatgroup"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6732347837:AAFVmDoWgRuT1UWqbhrbcgavMTE5vnfzrEw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "4M5PGYIIJV9P"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6231550362  # User id of your telegram account (Must be integer)

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
