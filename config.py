import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21941890")

API_HASH = os.environ.get("API_HASH", "a192de10945cf3685dbe8ae711b238d8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5924930700:AAGzwKII18ALChOJuPxMWeUhy_LRP6CIPQA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "RenameBotGroup") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Chiku:Harsh9421806556@cluster0.wc5jn4k.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/3a4419ae75ee578ade2b3.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1366318700').split()]

PORT = os.environ.get("PORT", "8080" )
