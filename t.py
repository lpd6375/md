import MySQLdb
import configparser

from tootchina import settings

nest = "9a0b75a5-cb17-4f92-965b-816a93b606cd"
north = "8c8c79d0-ce80-421d-abe8-31dc446b3371"
cf = configparser.ConfigParser()
cf.read(settings.CONF_DIR)
host = cf.get('client',"db_host")
user = cf.get("client","db_user")
passwd=cf.get("client","db_passwd")


def getsqlrun(sql):
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db='totte', port=3306,use_unicode=True,charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.close()
    return  cur


sql = "SELECT * FROM campus where campus_id not in ('9a0b75a5-cb17-4f92-965b-816a93b606cd','8c8c79d0-ce80-421d-abe8-31dc446b3371')"

print(sql)
getsqlrun(sql)

sql0 = f'''SELECT b.*,( @ro := @ro + 1 ) AS rank FROM	(	SELECT DISTINCT	( student_extra.cate_one_number + student_extra.cate_two_number + student_extra.cate_three_number + student_extra.cate_four_number + student_extra.cate_five_number ) AS sum 
	FROM
		student_extra,
		student 
	WHERE
		student.student_id = student_extra.student_id 
		AND student.campus_id NOT IN ( '{nest}', '{north}' ) 
		AND student.`name` NOT LIKE '试听%' 
	ORDER BY
		sum DESC 
	) b,
	( SELECT @ro := 0 ) c'''
print(sql0)
out = getsqlrun(sql0)
for i in out:
    print(i)