from importlib.metadata import entry_points
from telegram import *
from telegram.ext import *

from integrated_definition import *

class Cow_RG():
    def __init__(self, db) -> None:
        self.db = db

        self.cow_register_handler = ConversationHandler(
            entry_points = [CommandHandler('cow',self.Cow_Region_select)],
            states={
                REGION_SELECT : [CallbackQueryHandler(self.Cow_number_input)],
                COW_INPUT : [MessageHandler(Filters.text, self.Cow_number_output)],
                PRAGMENT_ : [CallbackQueryHandler(self.Cow_estrous)],
                ESTROUS_ : [CallbackQueryHandler(self.Cow_end)]

            },
            fallbacks=[
                CommandHandler('cancel',self.cancel)
            ]
        )

    def get_handler(self) -> Dispatcher:
        return self.cow_register_handler

    #등록할 소의 축사 번호 선택
    def Cow_Region_select(self, update, context):
        self.u_id  = update.effective_chat.id

        #데이터베이스에서 부지명 가져오기(입력값 : self.u_id)
        #region_list = []
        buttons = []

        #부지 수에 따른 버튼 생성(데이터베이스에 들어있음 : 지역)
        for rg in region_list:
            buttons.append([KeyboardButton(text = rg)],)

        keyboard = ReplyKeyboardMarkup(buttons,one_time_keyboard=True)

        context.bot.send_message(self.u_id,text = "기능을 선택해주세요",\
            reply_markup = keyboard)

        # update.callback_query.answer()
        # update.callback_query.edit_message_text(text,reply_markup = keyboard)

        return REGION_SELECT

    #등록할 소의 번호 입력
    def Cow_number_input(self, update, context):
        context.bot.send_message(self.u_id,text = "소 등록번호를 입력해주세요")

        return COW_INPUT
        

    #등록할 소의 번호 데이터베이스 저장
    def Cow_number_output(self, update, context):
        input_data = update.message.text
        #text 입력 받은후 데이터베이스 저장 코드 필요

        context.bot.send_message(self.u_id,text = "소 등록번호 입력이 완료되었습니다.")
        

        return self.Cow_pragment(update, context)

    #소 임신 여부
    def Cow_pragment(self, update, context):
        pragment_list = ['O', 'X']
        buttons = []

        for pr in pragment_list:
            buttons.append([KeyboardButton(text = pr)],)

        keyboard = ReplyKeyboardMarkup(buttons,one_time_keyboard=True)

        context.bot.send_message(self.u_id,text = "임신여부를 선택해주세요",\
            reply_markup = keyboard)
        # update.callback_query.answer()
        # update.callback_query.edit_message_text(text,reply_markup = keyboard)
        
        return PRAGMENT_

    #소 발정 여부
    def Cow_estrous(self, update, context):
        estrous_list = ['O', 'X']
        buttons = []

        for es in estrous_list:
            buttons.append([KeyboardButton(text = es)],)

        keyboard = ReplyKeyboardMarkup(buttons,one_time_keyboard=True)

        context.bot.send_message(self.u_id,text = "발정여부를 선택해주세요",\
            reply_markup = keyboard)
        # update.callback_query.answer()
        # update.callback_query.edit_message_text(text,reply_markup = keyboard)

        return ESTROUS_
        
    #소 입력 끝 , 입력한 소 정보 보여주기
    def Cow_end(self, update, context):
        context.bot.send_message(self.u_id,text = "모든 정보 입력이 완료되었습니다.")
        # update.callback_query.answer()
        # update.callback_query.edit_message_text(text,reply_markup = keyboard)
        return self.cancel(update, context)

    def cancel(self, update, context):
        """Display the gathered info and end the conversation."""
        context.user_data.clear()
        update.message.reply_text("종료 되었습니다.")
        update.message.reply_text("새로 시작하시려면 /start 명령어를 사용하세요.")

        return ConversationHandler.END