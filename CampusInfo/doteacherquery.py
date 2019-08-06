



# 获取老师基本信息，姓名、校区、工号
from tootchina.sqltool import get_sql_done


def getteacherbasicinfo(request):
    serial = request.Get.get("serial")
    sql = f"""
    SELECT
    employee.`name`,
    employee.serial,
    campus.campus_name
    FROM
    employee ,
    campus
    WHERE
    employee.campus_id = campus.campus_id AND
    employee.serial = '{serial}'
    """
    cur = get_sql_done(sql)
    for item in cur:
        li = item
    print(li)

def getteachersallcourse():
    pass


# 获取老师卡牌明细，返回一个二维数组？
def getteachercard(request):
    serial  = request.GET.get("serial")
    sql = f"""
    SELECT
    Count(student_card.card_num) AA,
    card.card_name
    FROM
    student_card ,
    card
    WHERE
    student_card.employee_id = (SELECT employee.employee_id FROM employee WHERE employee.serial = '{serial}') AND
    student_card.card_id = card.id
    GROUP BY
    student_card.card_id
    ORDER BY AA DESC 
    """