import logging
import os
import pymysql
import sys

from telegram import *
from telegram.ext import *
from global_variable import *
from database.db_manager import DBManager
from database.db_insert import DBInsert
from database.config import *
from database.db_select import *
from database.db_delete import *



class Farm():
    def __init__(self):

        con = DBManager.connect()

        self.farm_handler = ConversationHandler(
            entry_points = [CommandHandler('farm',self.farm_select)],
            states = {
                CLICK_BUTTON : [CallbackQueryHandler(self.farm_num)],
                FARM_NUM : [MessageHandler(Filters.text & ~Filters.command, self.farm_add)],
                FARM_NAME : [MessageHandler(Filters.text & ~Filters.command, self.farm_image)],
                FARM_DELETE :  [CallbackQueryHandler(self.farm_delete)],
            },
            fallbacks = [CommandHandler('cancel',self.cancel)],

            map_to_parent={
                ConversationHandler.END:ConversationHandler.END
            }
        )


    def get_handler(self) -> Dispatcher:
        return self.farm_handler


    # 부지 메뉴 버튼 디자인
    def build_menu(self, buttons, n_cols, header_buttons=None, footer_buttons=None):
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, header_buttons)
        if footer_buttons:
            menu.append(footer_buttons)

        return menu


    #부지 메뉴 시작
    def farm_select(self, update:Update, context:CallbackContext) -> None:

        self.user_id = update.effective_chat.id
        btn_list = []
        btn_list.append(InlineKeyboardButton("부지 확인", callback_data="1"))
        btn_list.append(InlineKeyboardButton("부지 추가", callback_data="2"))
        btn_list.append(InlineKeyboardButton("부지 삭제", callback_data="3"))

        show_markup = InlineKeyboardMarkup(self.build_menu(btn_list, len(btn_list)))
  
        
        update.message.reply_text("선택", reply_markup = show_markup)

        return CLICK_BUTTON


    #부지 버튼 리턴값
    def farm_num(self,update:Update, context:CallbackContext) -> None:
        
        query = update.callback_query.data
    
        if query == "1":
            return self.farm_confirm(update, context)
        
        elif query == "2":
            return self.farm_info_num(update, context)

        elif query == "3":
            return self.farm_delete_confirm(update, context)




    def cancel(self, update: Update, context: CallbackContext):
        """Display the gathered info and end the conversation."""

        context.user_data.clear()
        update.message.reply_text("종료 되었습니다.")
        update.message.reply_text("새로 시작하시려면 /start 명령어를 사용하세요.")

        return ConversationHandler.END

    #부지 확인
    def farm_confirm(self, update: Update, context: CallbackContext) -> None:

        self.chat_id = update.effective_chat.id

        self.show_list = []
        self.data_list = []
        self.select_one_value = ['farm_name' ]

        data = DBSelect.one_search_key('farm_info', ['farm_name',] , 'farm_no', str(self.chat_id))

        for i in data:
            self.data_list.append(i[0])

        for i in range(len(self.data_list)):
            self.show_list.append([InlineKeyboardButton(f"{self.data_list[i]}",url = 
            'https://thumbs.dreamstime.com/z/minsk-district-belarus-may-inside-interi\
            or-cowshed-cows-full-degree-panorama-minsk-district-belarus-may-138801640.jpg')])


        show_markup = InlineKeyboardMarkup(self.show_list)
        
        context.bot.send_message(self.user_id,"나의 부지", reply_markup=show_markup)

    #========================================================================

    # 부지 추가

    def farm_info_num(self, update:Update, context:CallbackContext) -> None:

        update.callback_query.message.edit_text('부지 번호를 입력해주세요.')
        
        return FARM_NUM

    def farm_add(self, update:Update, context:CallbackContext) -> None:

        #TEST#
        context.user_data['farm'] = []
        context.user_data['farm'].append(update.message.text)
        
        update.message.reply_text('부지 이름을 입력해주세요.')
        
        return FARM_NAME


    def farm_image(self, update:Update, context:CallbackContext):

        context.user_data['farm'].append(update.message.text)
        context.user_data['farm'].append("row")


        DBInsert.table('farm_info', farm_info_cols, context.user_data['farm'], False)

        # file_path = os.path.join(self.dir_now, context.user_data['farm_name']+".png")
        # photo_id = update.message.photo[-1].file_id  
        # photo_file = context.bot.getFile(photo_id)
        # photo_file.download(file_path)
        update.message.reply_text('저장 완료')
        update.message.reply_text("새로 시작하시려면 /start 명령어를 사용하세요.")

        return ConversationHandler.END
    #==================================================================


    #부지 삭제 

    def farm_delete_confirm(self, update: Update, context: CallbackContext) -> None:


        self.show_list = []
        self.data_list = []
        self.select_one_value = ['farm_name' ]

        data = DBSelect.selectAll('farm_info', self.select_one_value)

        for i in data:
            self.data_list.append(i[0])

        for i in range(len(self.data_list)):
            self.show_list.append([InlineKeyboardButton(f"{self.data_list[i]}",\
                callback_data=f"{self.data_list[i]}")])
     
        show_markup = InlineKeyboardMarkup(self.show_list)
        
        context.bot.send_message(self.user_id,"삭제할 부지를 선택해 주세요", reply_markup=show_markup)

        return FARM_DELETE



    def farm_delete(self,  update: Update, context: CallbackContext) -> None:

        query = update.callback_query.data
        one_delete_key = "farm_name"
      
        DBDelete.one_delete_key('farm_info',one_delete_key, query)


        update.callback_query.message.edit_text(f"{query} 삭제 완료")
        update.callback_query.message.edit_text("새로 시작하시려면 /start 명령어를 사용하세요.")
    
        return ConversationHandler.END
    #================================================================

