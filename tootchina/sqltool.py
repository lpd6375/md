import configparser
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
