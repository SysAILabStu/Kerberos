from cgitb import text
from tkinter import END
from telegram import *
from telegram.ext import *

from integrated_definition import *
from function_handler import *

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

class IntegrateMANAGER():
    def __init__(self, update_token,function_list) -> None:
        self.updater = Updater(update_token)
        self.dispatcher = self.updater.dispatcher

        self.function_list = function_list

    def cancel(self, update: Update, context: CallbackContext) -> int:
        """Display the gathered info and end the conversation."""
        context.user_data.clear()
        update.message.reply_text("취소 되었습니다.")
        return ConversationHandler.END

    def main(self):

        for function in self.function_list:
            handler = FunctionHandler(self.function_list)
            self.dispatcher.add_handler(handler.get_conv_handler())

        # self.dispatcher.add_handler(WorkSheetHandler.get_handler)

        self.dispatcher.add_handler(CommandHandler("cancel", self.cancel))

        self.updater.start_polling()
        self.updater.idle()

        