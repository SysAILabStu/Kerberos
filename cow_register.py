from importlib.metadata import entry_points
from database.db_select import *
from database.db_insert import *
from database.db_update import *
from database.config import *
from telegram import *
from telegram.ext import *

import datetime

from integrated_definition import *

class Cow_RG():
    def __init__(self) -> None:

        self.cow_register_handler = ConversationHandler(
            entry_points = [CommandHandler('cow',self.Cow_Region_select)],
            states={
                REGION_SELECT : [CallbackQueryHandler(self.Cow_number_input,pattern='^(?!' + str(END) + ').*$')],
                COW_INPUT : [MessageHandler(Filters.text, self.Cow_number_output)],
                PRAGMENT_ : [CallbackQueryHandler(self.Cow_estrous,pattern='^(?!' + str(END) + ').*$')],
                ESTROUS_ : [CallbackQueryHandler(self.Cow_end,pattern='^(?!' + str(END) + ').*$')]

            },
            fallbacks=[
                CommandHandler('cancel',self.cancel)
            ],
            map_to_parent={
                ConversationHandler.END:ConversationHandler.END
            }
        )

    def get_handler(self) -> Dispatcher:
        return self.cow_register_handler

    #등록할 소의 축사 번호 선택
    def Cow_Region_select(self, update: Update, context: CallbackContext)->str:
        self.u_id  = update.effective_chat.id
    
        #데이터베이스에서 부지명 가져오기(입력값 : self.u_id)
        region_list =DBSelect.one_search_key('farm_info', ['farm_name',] , 'farm_no', str(self.u_id))[0]

        buttons = []
        if region_list:
            #부지 수에 따른 버튼 생성(데이터베이스에 들어있음 : 지역)
            for rg in region_list:
                buttons.append([InlineKeyboardButton(text = rg, callback_data = rg)],)

            keyboard = InlineKeyboardMarkup(buttons,one_time_keyboard=True)

            context.bot.send_message(self.u_id,text = "부지를 선택해주세요",\
                reply_markup = keyboard)
            # text = '부지를 선택해주세요'
            # update.callback_query.answer()
            # update.callback_query.edit_message_text(text,reply_markup = keyboard)

            return REGION_SELECT
        
        else:
            context.bot.send_message(self.u_id,text = "부지를 먼저 입력해주세요\n 재사작'/start")
            return ConversationHandler.END

    #등록할 소의 번호 입력
    def Cow_number_input(self, update: Update, context: CallbackContext) -> int:
        print("!!!!!!!!")
        region_data = update.callback_query.data
        print(f'{region_data}선택한 부지')
        # context.bot.send_message(self.u_id,text = "소 등록번호를 입력해주세요")
        text = '소 등록번호를 입력해주세요(삽입/수정)'
        update.callback_query.answer()
        update.callback_query.edit_message_text(text)

        return COW_INPUT
        

    #등록할 소의 번호 데이터베이스 저장
    def Cow_number_output(self, update: Update, context: CallbackContext):
        input_data = update.message.text
        context.user_data[COW_INPUT] = input_data
        #text 입력 받은후 데이터베이스 저장 코드 필요
        print(f'{input_data}입력한 소등록번호')

        #없어도 되는 텍스트
        context.bot.send_message(self.u_id,text = "소 등록번호 입력이 완료되었습니다.")
        

        return self.Cow_pragment(update, context)

    #소 임신 여부
    def Cow_pragment(self, update: Update, context: CallbackContext)->str:
        pragment_list = ['O', 'X']
        buttons = []

        for pr in pragment_list:
            buttons.append([InlineKeyboardButton(text = pr, callback_data = pr)],)

        keyboard = InlineKeyboardMarkup(buttons,one_time_keyboard=True)

        context.bot.send_message(self.u_id,text = "임신여부를 선택해주세요",\
            reply_markup = keyboard)
        
        return PRAGMENT_

    #소 발정 여부
    def Cow_estrous(self, update: Update, context: CallbackContext)->str:
        pragment_data = update.callback_query.data
        print(f'{pragment_data}임신여부 선택')

        if pragment_data == 'O':
            context.user_data[PRAGMENT_] = datetime.datetime.now().strftime("%y-%m-%d")
        else:
            context.user_data[PRAGMENT_] = '0-0-0'
        estrous_list = ['O', 'X']
        buttons = []

        for es in estrous_list:
            buttons.append([InlineKeyboardButton(text = es, callback_data = es)],)

        keyboard = InlineKeyboardMarkup(buttons,one_time_keyboard=True)

  
        text =  "발정여부를 선택해주세요"
        update.callback_query.answer()
        update.callback_query.edit_message_text(text,reply_markup = keyboard)

        return ESTROUS_
        

    #소 입력 끝 , 입력한 소 정보 보여주기
    def Cow_end(self, update: Update, context: CallbackContext)->str:
        estrous_data = update.callback_query.data
        print(f'{estrous_data}발정여부')

        if estrous_data == 'O':
            context.user_data[ESTROUS_] = datetime.datetime.now().strftime("%y-%m-%d")
        else:
            context.user_data[ESTROUS_] = '0-0-0'
            
        print([str(self.u_id),context.user_data[COW_INPUT],context.user_data[PRAGMENT_],context.user_data[ESTROUS_]])

        if DBSelect.two_search_keys('farm_detail',['cow_no'],['farm_no','cow_no',] ,[self.u_id,context.user_data[COW_INPUT],]):
            DBUpdate.update('farm_detail',['cow_pregnant','cow_estrous',],[context.user_data[PRAGMENT_],context.user_data[ESTROUS_]],['farm_no','cow_no'],\
                [str(self.u_id),context.user_data[COW_INPUT]])
        else:
            if context.user_data[PRAGMENT_] != None and context.user_data[ESTROUS_] == None : 
                DBInsert.table('farm_detail', farm_detail_cols,[str(self.u_id),context.user_data[COW_INPUT],context.user_data[PRAGMENT_]],True, False)
            elif context.user_data[PRAGMENT_] == None and context.user_data[ESTROUS_] != None:
                DBInsert.table('farm_detail', farm_detail_cols,[str(self.u_id),context.user_data[COW_INPUT],context.user_data[ESTROUS_]], False,True)
            elif context.user_data[PRAGMENT_] != None and context.user_data[ESTROUS_] != None:
                DBInsert.table('farm_detail',farm_detail_cols, [str(self.u_id),context.user_data[COW_INPUT],context.user_data[PRAGMENT_],context.user_data[ESTROUS_]], True,True)
            else:
                DBInsert.table('farm_detail', farm_detail_cols,[str(self.u_id),context.user_data[COW_INPUT]], False, False)

        context.bot.send_message(self.u_id,text = f"모든 정보 입력이 완료되었습니다.\n재시작을 원하신다면 '/start'를 눌러주세요")
        # update.callback_query.answer()
        # update.callback_query.edit_message_text(text,reply_markup = keyboard)
        return ConversationHandler.END

    def cancel(self, update: Update, context: CallbackContext):
        """Display the gathered info and end the conversation."""
        context.user_data.clear()
        update.message.reply_text("종료 되었습니다.")
        update.message.reply_text("새로 시작하시려면 /start 명령어를 사용하세요.")

        return ConversationHandler.END