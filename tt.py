from typing import List

import MySQLdb
import configparser
from MySQLdb.cursors import Cursor

from tootchina import settings

cf = configparser.ConfigParser()
cf.read(settings.CONF_DIR)
host = cf.get('client', "db_host")
user = cf.get("client", "db_user")
passwd = cf.get("client", "db_passwd")


def get_sql_done(sql) -> Cursor:
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db='totte', port=3306, use_unicode=True, charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.close()
    return cur


def get5sumbase(serial) -> List:
    sql = f"""
    SELECT
	student_extra.cate_one_number,
	student_extra.cate_two_number,
	student_extra.cate_three_number,
	student_extra.cate_four_number,
	student_extra.cate_five_number,
	( student_extra.cate_one_number + student_extra.cate_two_number + student_extra.cate_three_number + student_extra.cate_four_number + student_extra.cate_five_number) AS card_sum 
    FROM
	student_extra,
	student 
    WHERE
	student_extra.student_id = student.student_id 
	AND student.serial = '{serial}'
    """
    cur = get_sql_done(sql)
    return cur


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

    # print(blist)
    # print(allrank)
    relist = [allrank[0].index(blist[0])+1,allrank[1].index(blist[1])+1,allrank[2].index(blist[2])+1, allrank[3].index(blist[3])+1,allrank[4].index(blist[4])+1 ,allrank[5].index(blist[5])+1 ]
    print(relist)
getclassrank('S00494')
