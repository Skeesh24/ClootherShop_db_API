import configparser

# you should make a creds.ini in the '/utils' and paste into it ur credentials
config = configparser.ConfigParser()
config.read("utils\\creds.ini")

# ============= export ============= #
config = config["DEFAULT"]
SQLALCHEMY_DATABASE_URL = f"postgresql://{config['user']}:{config['pwd']}@{config['host']}:{config['port']}/{config['name']}"
# ================================== #
