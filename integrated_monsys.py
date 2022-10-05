from turtle import update
from config import *
from database.db_manager import DBManager
from integrated_mg import IntegrateMANAGER
from telegram import *
from telegram.ext import *


#기능추가는 /영어
function_list = ['/farm','/cow','/doctor']

db = DBManager.connect
#sh자리에 데이터베이스 투입
im = IntegrateMANAGER(TELEGRAM_TOKEN,function_list)

im.main()

