ip = '203.230.103.188'
user = 'hyeongi'
pwd = '0000'
database = 'createfusioncontest'
opt = 'maria'

farm_detail_cols = ["farm_no", "cow_no", "cow_estrous", "cow_pregnant"]
owner_cols = ["telegram_id", "farm_no"]
doctor_cols = ["doctor_name", "doctor_phone", "doctor_mail"]
farm_info_cols = ["farm_no", "farm_name", "farm_image"]


import os

#if os.path.isfile("./instance/config.py"):
#  from instance.config import 