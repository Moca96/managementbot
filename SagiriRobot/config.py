class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 26405281
    API_HASH = "77b54622ef8e0fd15555d939fc74005d"

    CASH_API_KEY = "M0939R4PDIA291MR"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  
    
    EVENT_LOGS = (-1001982108661)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://zadkiel:zadkiel@zadkiel.rh8o93y.mongodb.net/?retryWrites=true&w=majority&appName=Zadkiel"  # Get this value from cloud.mongodb.com

    REDIS_URL = "redis://default:kMaLb8lDTzdf3MVW4gXmkcSaToV4hYci@redis-19240.c301.ap-south-1-1.ec2.cloud.redislabs.com:19240"  #Get this value from redis.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/31077a464a4ca165eb8bc.jpg"

    PM_START_IMG = "https://te.legra.ph/file/6201d9711b4703fd9e254.jpg"

    SUPPORT_CHAT = "zadkiel_hub"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "8981U7UV1QBH"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7012420639  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = [6058139652]  # User id of dev users
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
