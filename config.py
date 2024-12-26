import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7633818980:AAExSfhjq8D65YgZHX0IKtCsrFKlYL_S_i8")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21707980"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c7fbf41f913ac44d9a051f44a996b4c4")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7619883425"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vaibhavprajapati369:mji73ybYWYZK03Lz@cluster0.i50vm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
