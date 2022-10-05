from db_insert import DBInsert
from config import *

value = ['1131', '1']

DBInsert.table('farm', farm_cols, value, False)