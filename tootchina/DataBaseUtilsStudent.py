import configparser
import json
from typing import List

import MySQLdb
from MySQLdb.cursors import Cursor

from tootchina import settings

cf = configparser.ConfigParser()
cf.read(settings.CONF_DIR)
host = cf.get('client', "db_host")
user = cf.get("client", "db_user")
passwd = cf.get("client", "db_passwd")


# 与数据库建立连接并执行传入的语句返回查询结果
def get_sql_done(sql) -> Cursor:
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db='totte', port=3306, use_unicode=True, charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.close()
    return cur


def get_nation_rank() -> List:
    sql0 = f'''SELECT b.*,( @ro := @ro + 1 ) AS rank FROM	(	SELECT DISTINCT	( student_extra.cate_one_number + student_extra.cate_two_number + student_extra.cate_three_number + student_extra.cate_four_number + student_extra.cate_five_number ) AS sum 
        FROM
            student_extra,
            student 
        WHERE
            student.student_id = student_extra.student_id 
            AND student.campus_id NOT IN ( '9a0b75a5-cb17-4f92-965b-816a93b606cd','8c8c79d0-ce80-421d-abe8-31dc446b3371' ) 
            AND student.`name` NOT LIKE '试听%' 
        ORDER BY
            sum DESC 
        ) b,
        ( SELECT @ro := 0 ) c'''
    out = get_sql_done(sql0)
    list = []
    for i in out:
        list.append(i[0])
    #  反回一个从到小的卡牌数据列表，排名可用 index() 方法获得
    return list


# 获取学生个人信息，姓名，学号，班级，校区以及班级人数
def get_student_basic_info(serial) -> List:
    serial = 'S01840'
    sql = f"""SELECT
    student.`name`,
    student.serial,
    stu_class.`name` AS class,
    b.class_cnt,
    campus.campus_name
    FROM
    student ,
    stu_class_current ,
    stu_class ,
    campus,
    (SELECT
    Count(stu_class_current.class_id) class_cnt
    FROM
    stu_class_current
    WHERE
    stu_class_current.class_id = (SELECT
    stu_class.class_id
    FROM
    student ,
    stu_class ,
    stu_class_current
    WHERE
    student.serial = '{serial}' AND
    student.student_id = stu_class_current.student_id AND
    stu_class_current.class_id = stu_class.class_id)) b
    WHERE
    student.student_id = stu_class_current.student_id AND
    stu_class_current.class_id = stu_class.class_id AND
    stu_class.campus_id = campus.campus_id AND
    student.serial = '{serial}'"""
    cur = get_sql_done(sql)
    row_headers = [x[0] for x in cur.description]
    json_data = []
    for result in cur:
        json_data.append(dict(zip(row_headers, result)))
    print(json.dumps(json_data, ensure_ascii=False, indent=4))



# 得到学生五类卡牌及总数顺序为1，2，3，4，5，总数
def get5sumbase(serial) -> List:
    sql = f"""
    SELECT
	student_extra.cate_one_number,
	student_extra.cate_two_number,
	student_extra.cate_three_number,
	student_extra.cate_four_number,
	student_extra.cate_five_number,
	( student_extra.cate_one_number + student_extra.cate_two_number + student_extra.cate_three_number + student_extra.cate_four_number + student_extra.cate_five_number + student_extra.cate_one_number ) AS card_sum 
    FROM
	student_extra,
	student 
    WHERE
	student_extra.student_id = student.student_id 
	AND student.serial = '{serial}'
    """
    cur = get_sql_done(sql)
    return cur



# 返回学生五类卡牌数量及总量
def get5sum(serial):
    cur = get5sumbase(serial)
    row_headers = [x[0] for x in cur.description]
    json_data = []
    for result in cur:
        json_data.append(dict(zip(row_headers, result)))
    print(json.dumps(json_data, ensure_ascii=False, indent=4))


# 反回查询学生的各类卡 牌排名信息顺序为（1，2，3，4，5）
def getcatenationrank(serial):
    tlist = []
    listcatenationrank = []
    for cate in ('cate_one_number', 'cate_two_number', 'cate_three_number', 'cate_four_number', 'cate_five_number'):
        sql = f"""
            SELECT DISTINCT
            student_extra.{cate}
            FROM
            student_extra ,
            student
            WHERE
            student_extra.student_id = student.student_id 
            AND
            student.campus_id NOT IN ('9a0b75a5-cb17-4f92-965b-816a93b606cd','8c8c79d0-ce80-421d-abe8-31dc446b3371')
            ORDER BY
            student_extra.{cate} DESC
            """
        cur = get_sql_done(sql)
        seplist = []
        for i in cur:
            seplist.append(i[0])
        tlist.append(seplist)
    out = get5sumbase(serial)
    for item in out:
        listcatenationrank = item
    nationranklist = get_nation_rank()
    relist = [tlist[0].index(listcatenationrank[0]) + 1, tlist[1].index(listcatenationrank[1]) + 1,
              tlist[2].index(listcatenationrank[2]) + 1, tlist[3].index(listcatenationrank[3]) + 1,
              tlist[4].index(listcatenationrank[4]) + 1, nationranklist.index(listcatenationrank[5]) + 1]
    print(relist)


'''    '''


def getclassrank(serial):
    allrank = []
    for item in (
            'a.cate_one_number', 'a.cate_two_number', 'a.cate_three_number', 'a.cate_four_number', 'a.cate_five_number',
            '(a.cate_one_number+a.cate_two_number+a.cate_three_number+a.cate_four_number+ a.cate_five_number)'):
        sql = f"""SELECT
            {item}        
            FROM
            student_extra a
            WHERE
            a.student_id IN (SELECT
            stu_class_current.student_id
            FROM
            stu_class_current
            WHERE
            stu_class_current.class_id = (SELECT
            stu_class_current.class_id
            FROM
            student ,
            stu_class_current
            WHERE
            student.serial = '{serial}' AND
            student.student_id = stu_class_current.student_id))  
        """
        cur = get_sql_done(sql)
        seprank = []
        for cr in cur:
            seprank.append(cr[0])
            seprank.sort(reverse=True)
        allrank.append(seprank)
    bcur = get5sumbase(serial)
    blist = []
    for isb in bcur:
        blist = list(isb)
    relist = [allrank[0].index(blist[0])+1,allrank[1].index(blist[1])+1,allrank[2].index(blist[2])+1, allrank[3].index(blist[3])+1,allrank[4].index(blist[4])+1 ,allrank[5].index(blist[5])+1 ]
