from telegram import *
from telegram.ext import *

from integrated_definition import *

from cow_register import *

class FunctionHandler():
    def __init__(self,function_list,db) -> None:
        self.db = db
        self.function_list = function_list

        #기능별 Handler부착
        self.handlers = [Cow_RG(self.db)]

    def get_conv_handler(self):
        self.conv_handlers = [x.get_handler() for x in self.handlers]
        
        conv = ConversationHandler(
            entry_points=[ 
                CommandHandler("start", self.keyboard_in_button)
                ],
            states={
                SELECT: self.conv_handlers
                },
            fallbacks=[
                CommandHandler('cancel', self.cancel), 
                MessageHandler(Filters.command, self.unknown)
                ],
            map_to_parent={
                ConversationHandler.END:ConversationHandler.END
            }
        )
        return conv

    def cancel(self, update: Update, context: CallbackContext) -> int:
        """Display the gathered info and end the conversation."""
        context.user_data.clear()
        update.message.reply_text("취소 되었습니다.")
        update.message.reply_text("새로 시작하시려면 /start 명령어를 사용하세요.")
        return ConversationHandler.END
    
    def unknown(self, update: Update, context: CallbackContext) -> int:
        context.user_data.clear()
        update.message.reply_text("잘 이해하지 못하였습니다.")
        return ConversationHandler.END


    def keyboard_in_button(self, update:Update, context:CallbackContext)->str:
        user_id = update.effective_chat.id

        buttons = []

        for function in self.function_list:
            buttons.append([KeyboardButton(text = function)],)

        keyboard = ReplyKeyboardMarkup(buttons,one_time_keyboard=True)

        context.bot.send_message(user_id,text = "기능을 선택해주세요",\
            reply_markup = keyboard)

        return SELECT
   
        
