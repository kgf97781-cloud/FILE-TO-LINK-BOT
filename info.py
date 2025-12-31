from os import environ, getenv
from Script import script

# 🚀 __Bot Configuration__
SESSION = environ.get('SESSION', 'RexBots')  # Session name
API_ID = int(environ.get('API_ID', '38484181'))
API_HASH = environ.get('API_HASH', '004516cc7835d8a332e1cb5717393ff3')
BOT_TOKEN = environ.get('BOT_TOKEN', '8544909981:AAGLDNaAp9Fth8B77Q3qXn23FU7q31ToZHI')

# 👑 __Owner & Admins__
ADMINS = [int(i) for i in environ.get('ADMINS', '5816147544').split()]
AUTH_CHANNEL = [int(i) for i in environ.get("AUTH_CHANNEL", "-1002573510673").split()]
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'Toonworld4all_Tamil')
BOT_USERNAME = environ.get("BOT_USERNAME", 'Toonworld4all_Tamil')

# 🔗 __Channel & Support Links__
CHANNEL = environ.get('CHANNEL', 'https://t.me/toonworld4all_Tamil')
SUPPORT = environ.get('SUPPORT', 'https://t.me/toonworld4all_Tamil')
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/toonworld4all_Tamil')
HOW_TO_OPEN = environ.get('HOW_TO_OPEN', 'https://t.me/toonworld4all_Tamil')

# 📢 __Log Channels__
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-1002573510673'))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1002573510673'))
PREMIUM_LOGS = int(environ.get("PREMIUM_LOGS", '-1002573510673'))
VERIFIED_LOG = int(environ.get('VERIFIED_LOG', '-1002573510673'))
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1002573510673"))

# ✅ __Feature Toggles__
VERIFY = False  # Enable user verification
FSUB = environ.get("FSUB", True)  # Force Subscribe
ENABLE_LIMIT = environ.get("ENABLE_LIMIT", True)
BATCH_VERIFY = False
IS_SHORTLINK = False
MAINTENANCE_MODE = environ.get("MAINTENANCE_MODE", False)
PROTECT_CONTENT = environ.get('PROTECT_CONTENT', False)
PUBLIC_FILE_STORE = environ.get('PUBLIC_FILE_STORE', True)
BATCH_PROTECT_CONTENT = environ.get('BATCH_PROTECT_CONTENT', False)

# 🔗 __Shortlink Configuration__
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')

# 💾 __Database Configuration__
DB_URL = environ.get('DATABASE_URI', "mongodb+srv://Bosshub:JMaff0WvazwNxKky@cluster0.l0xcoc1.mongodb.net/?appName=Cluster0")
DB_NAME = environ.get('DATABASE_NAME', "rexlinkbot")

# 📸 __Media & Images__
QR_CODE = environ.get('QR_CODE', 'https://ibb.co/mVkSySr7')
VERIFY_IMG = environ.get("VERIFY_IMG", "https://ibb.co/mVkSySr7")
AUTH_PICS = environ.get('AUTH_PICS', 'https://ibb.co/mVkSySr7')
PICS = environ.get('PICS', 'https://ibb.co/mVkSySr7')
FILE_PIC = environ.get('FILE_PIC', 'https://ibb.co/mVkSySr7')

# 📝 __Captions__
FILE_CAPTION = environ.get('FILE_CAPTION', script.CAPTION)
BATCH_FILE_CAPTION = environ.get('BATCH_FILE_CAPTION', script.CAPTION)
CHANNEL_FILE_CAPTION = environ.get('CHANNEL_FILE_CAPTION', script.CAPTION)

# ⏱️ __Time & Limits__
PING_INTERVAL = int(environ.get("PING_INTERVAL", 1200))
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', 60))
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", 600))
MAX_FILES = int(environ.get("MAX_FILES", 50))
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 60))  # Hours

# ⚙️ __Worker & App Config__
WORKERS = int(environ.get('WORKERS', 10))
MULTI_CLIENT = False
NAME = environ.get('name', 'rexbots_official')

# 🌐 __Web Server__
ON_HEROKU = 'DYNO' in environ
APP_NAME = environ.get('APP_NAME') if ON_HEROKU else None

PORT = int(environ.get('PORT', 2626))
NO_PORT = str(environ.get("NO_PORT", "true")).lower() in ("true", "1", "yes")
HAS_SSL = str(environ.get("HAS_SSL", "true")).lower() in ("true", "1", "yes")

# URL Generation
BIND_ADDRESS = environ.get("WEB_SERVER_BIND_ADDRESS", "")   ##without https:// paste the base url here 
FQDN = environ.get("FQDN", BIND_ADDRESS)

if not FQDN.startswith("http"):
    PROTOCOL = "https" if HAS_SSL else "http"
    PORT_SEGMENT = "" if NO_PORT else f":{PORT}"
    
    # Clean up trailing slashes for consistency
    FQDN = FQDN.rstrip('/')
    URL = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"
else:
    URL = FQDN

