import os
# Your AZURE settings
APPLICATION_ID = "-"
CLIENT_ID = "-"
CLIENT_SECRET = "-"
AUTHORITY = "https://login.microsoftonline.com/consumers"
AUTHORITY_URL = 'https://login.microsoftonline.com/consumers/'
REDIRECT_PATH = "/getAToken"
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'
SCOPE = ["User.ReadBasic.All"]
SESSION_TYPE = "filesystem"
REDIRECT_URI = "http://localhost:5000/getAToken"
#Your DB settings
db_host = 'localhost'
db_user = 'root'
db_password = 'root'
db_table = "library"
#Place your logo in base.html line:160
