from typing import List

import MySQLdb
import configparser

from tootchina import settings

nest = "9a0b75a5-cb17-4f92-965b-816a93b606cd"
north = "8c8c79d0-ce80-421d-abe8-31dc446b3371"
cf = configparser.ConfigParser()
cf.read(settings.CONF_DIR)
host = cf.get('client', "db_host")
user = cf.get("client", "db_user")
passwd = cf.get("client", "db_passwd")


def get_sql_done(sql):
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db='totte', port=3306, use_unicode=True, charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.close()
    return cur


#
# sql = "SELECT * FROM campus where campus_id not in ('9a0b75a5-cb17-4f92-965b-816a93b606cd','8c8c79d0-ce80-421d-abe8-31dc446b3371')"
#
#
# sql0 = f'''SELECT b.*,( @ro := @ro + 1 ) AS rank FROM	(	SELECT DISTINCT	( student_extra.cate_one_number + student_extra.cate_two_number + student_extra.cate_three_number + student_extra.cate_four_number + student_extra.cate_five_number ) AS sum
# 	FROM
# 		student_extra,
# 		student
# 	WHERE
# 		student.student_id = student_extra.student_id
# 		AND student.campus_id NOT IN ( '{nest}', '{north}' )
# 		AND student.`name` NOT LIKE '试听%'
# 	ORDER BY
# 		sum DESC
# 	) b,
# 	( SELECT @ro := 0 ) c'''
# # print(sql0)
# out = getsqlrun(sql0)
# list=[]
# for i in out:
#     list.append(i)
# print(list)
# for ii in list:
#     if ii[0]==8:
#         print(int(ii[1]))
#         break




def get_nation_rank() -> List:
    sql0 = f'''
    SELECT b.*,( @ro := @ro + 1 ) AS rank FROM (SELECT DISTINCT	( student_extra.cate_one_number + student_extra.cate_two_number + student_extra.cate_three_number + student_extra.cate_four_number + student_extra.cate_five_number ) AS sum 
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
    return list


def get5sumbase(serial):
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
    nationranklist= get_nation_rank()
    relist = [tlist[0].index(listcatenationrank[0])+1, tlist[1].index(listcatenationrank[1])+1,
              tlist[2].index(listcatenationrank[2])+1, tlist[3].index(listcatenationrank[3])+1,
              tlist[4].index(listcatenationrank[4])+1,nationranklist.index(listcatenationrank[5])+1 ]
    print(relist)


getcatenationrank(serial='S01840')
