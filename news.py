import logging
import os
import pymysql
import sys
import telegram


from telegram import *
from telegram.ext import *
from instance.config import *


class news():
    def __init__(self):
        
        # self.updater = Updater("5431097144:AAGt813IWJ_eDJVJjngYec0koEux9w_w8wI")
        # self.dispatcher = self.updater.dispatcher 

        self.farm_handler = CommandHandler('news',self.cow_news)        
        
    def get_handler(self) -> Dispatcher:

        return self.farm_handler


    def cow_news(self, update:Update, context:CallbackContext) -> None:

        self.chat_id = update.effective_chat.id
        context.bot.send_message(chat_id = f"{self.chat_id}",
        text = "[인공수정 장점](http://www.limc.co.kr/management/ManageReproduction_View.asp?category=2&num=26&GotoPage=1)", 
        parse_mode = 'Markdown',disable_web_page_preview="True")
        
        