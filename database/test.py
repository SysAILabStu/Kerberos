from db_select import DBSelect
from db_insert import DBInsert
from config import *


# 입력데이터 예시
farm_info_insertvalue = [1111, '진우네 농장', '-']
farm_detail_insertvalue = [2222, 281]
doctor_insertvalue = ['김현기', '010-1234-1234', 'edu@hanbat.ac.kr']
owner_insertvalue = [12348171, 1111]

# 조회데이터 예시
select_all_value = ['*', ]
select_one_value = ['farm_no', ]

one_search_key = 'farm_no'
one_search_data = 1111

# farm_info 테이블에 데이터 입력 예시
# DBInsert.table('farm_info', farm_info_cols, farm_info_insertvalue, False)

# farm_detail 테이블에 데이터 입력 예시
# DBInsert.table('farm_detail', farm_detail_cols, farm_detail_insertvalue, False)

# doctor 테이블에 데이터 입력 예시
# DBInsert.table('doctor', doctor_cols, doctor_insertvalue, False)

# owner 테이블에 데이터 입력 예시
# DBInsert.table('owner', owner_cols, owner_insertvalue, False)

# 테이블의 전체 데이터 조회 예시
# DBSelect.selectAll('farm_info', select_all_value)

# 조건 하나를 이용하여 데이터 조회 예시
# DBSelect.one_search_key('farm_info', select_one_value, one_search_key, one_search_data)
# DBSelect.one_search_key('farm_info', select_all_value, one_search_key, one_search_data)


