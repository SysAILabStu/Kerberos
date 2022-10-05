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

class Farm():
    def __init__(self):

        con = DBManager.connect()


        updater = Updater("5431097144:AAGt813IWJ_eDJVJjngYec0koEux9w_w8wI")
        dispatcher = updater.dispatcher 

        self.farm_handler = ConversationHandler(
            entry_points = [CommandHandler('start',self.farm_select)],
            states = {
                CLICK_BUTTON : [CallbackQueryHandler(self.farm_num)],
                FARM_NAME : [MessageHandler(Filters.text & ~Filters.command, self.farm_image)],
                FARM_CLICK : [MessageHandler(Filters.photo, self.farm_delete)]
            },
            fallbacks = [CommandHandler('cancel',self.cancel)],
        )

        dispatcher.add_handler(self.farm_handler)

        updater.start_polling()
        updater.idle()



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
            return self.farm_add(update, context)

        elif query == "3":
            return self.farm_confirm(update, context)



    def cancel(self, update: Update, context: CallbackContext) -> int:
        """Display the gathered info and end the conversation."""
        
        context.user_data.clear()
        update.message.reply_text("Cancel!")
        return ConversationHandler.END


    #부지 확인
    def farm_confirm(self, update: Update, context: CallbackContext) -> None:
        show_list = []
        for i in range(len(context.user_data['farm_name'])):
            # print(context.user_data['PHOTO_SAVE'][i].split(','))
            show_list.append([InlineKeyboardButton(f"{context.user_data['farm_name'][i]}",\
                callback_data=f"{context.user_data['farm_name'][i]}")])
        show_markup = InlineKeyboardMarkup(show_list)

        update.message.reply_text("나의 부지",reply_markup=show_markup)

        return FARM_CLICK
    #========================================================================

        
    # 부지 추가

    def farm_add(self, update:Update, context:CallbackContext) -> None:

        #TEST#

        context.user_data['farm_name'] = ['-']
    

        update.callback_query.message.edit_text('부지 이름을 입력해주세요.')

        
        return FARM_NAME


    def farm_image(self, update:Update, context:CallbackContext):


        
        context.user_data['farm_name'].append(update.message.text)
        context.user_data['farm_name'].append('test')


        DBInsert.table('farm_info', farm_info_cols, context.user_data['farm_name'], False)

        # file_path = os.path.join(self.dir_now, context.user_data['farm_name']+".png")
        # photo_id = update.message.photo[-1].file_id  
        # photo_file = context.bot.getFile(photo_id)
        # photo_file.download(file_path)
        # update.message.reply_text('사진 저장')

        return ConversationHandler.END
    #==================================================================


    #부지 삭제 
    def farm_delete(self,  update: Update, context: CallbackContext) -> None:
        query = update.callback_query.data

        file = f'{query}.png'

        if os.path.isfile(file):
            os.remove(file)
            context.user_data['farm_name'].remove(query)

        # context.bot.send_photo(chat_id=update.effective_user.id,photo=open(f"{photo_name}.png",'rb'))
        update.callback_query.message.edit_text(f"{query} 삭제 완료")
        return ConversationHandler.END
    #================================================================


kkk = Farm()

kkk.__init__()