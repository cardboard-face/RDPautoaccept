from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "1881742"))
    API_HASH = getenv("API_HASH", "9302cd0cff1e2aa81379d95aeba7f27b")
    BOT_TOKEN = getenv("BOT_TOKEN", "6078472433:AAE9iX1kyC9NNCJOBDivaPsi9QiNXEa_Sp8")
    FSUB = getenv("FSUB", "Hackinsider")
    CHID = int(getenv("CHID", "-1928008250"))
    SUDO = list(map(int, getenv("1353788579").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://zedteam21:PuvA0Slfpvu44OvS@cluster0.bzwi3j4.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
