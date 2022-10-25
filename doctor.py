import logging
import os
import pymysql
import sys
import telegram


from telegram import *
from telegram.ext import *
from instance.config import *


class Doctor():

    def __init__(self):

         self.doctor_handler = CommandHandler('doctor',self.doctor_num)


    def get_handler(self) -> Dispatcher:

        return self.doctor_handler


    def doctor_num(self, update:Update, context:CallbackContext) -> None:

        self.chat_id = update.effective_chat.id

        update.message.reply_text('의사 전화번호')
        context.bot.send_message(self.chat_id, "의사1: 010-3412-4398 \n의사2: 010-3414-4567")

    
        
        

