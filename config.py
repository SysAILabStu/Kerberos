TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"
GOOGLE_SERVICE_KEY = "YOUR_GOOGLE_KEY"
GOOGLE_SPREAD_SHEET = "YOUR_GOOGLE_SHEET"


import os
if os.path.isfile("instance/config.py"):
	from instance.config import *