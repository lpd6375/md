# 获取校区相关信息
from typing import List
from tootchina.sqltool import get_sql_done


# 获取校区ID、校区名称、校区编号
def getcampusnsn() -> List:
    sql = """
        SELECT
        campus.campus_id,
        SUBSTRING_INDEX(campus.campus_name, '（', 1)
        campus,
        SUBSTRING(campus.campus_name
        FROM - 6
        FOR
        5 ) num
        FROM
        campus
        WHERE
        campus.campus_id
        NOT
        IN('8c8c79d0-ce80-421d-abe8-31dc446b3371', '9a0b75a5-cb17-4f92-965b-816a93b606cd')"""
    cur = get_sql_done(sql)
    li = []
    for i in cur:
        li.append(list(i))
    return li


# 获取校区基本信息学生人数、卡牌总数、卡牌学生平均数（不分大类）。只返回学生ID和对应的卡牌总数，相关计算同前是端进行。
# [student_is,nrank,1,2,3,4,5] 列表结构
def getcampusbasicinfo(quest) -> List:
    campus_id = quest.GET.get("campus_id")
    sql = f"""SELECT
        student.student_id,
        (student_extra.cate_one_number+
        student_extra.cate_two_number+
        student_extra.cate_three_number+
        student_extra.cate_four_number+
        student_extra.cate_five_number) AS amount,
        student_extra.cate_one_number,
        student_extra.cate_two_number,
        student_extra.cate_three_number,
        student_extra.cate_four_number,
        student_extra.cate_five_number
        FROM
        student ,
        student_extra
        WHERE
        student.student_id = student_extra.student_id AND
        student.campus_id = '{campus_id}'
        ORDER BY amount DESC"""
    cur = get_sql_done(sql)
    li = []
    for i in cur:
        li.append(list(i))
    return li


# TODO:
#     1.完成校区相关信息的展示包括学生数量、学生人数分数布、学生全国排名情况
#     2.校区人数排名什么的，放到前端去处理这里把用到的给传过去就行了。
