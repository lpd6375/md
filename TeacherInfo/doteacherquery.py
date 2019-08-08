# 获取老师基本信息，姓名、校区、工号
from typing import List

from tootchina.sqltool import get_sql_done


def getcardname() -> List:
    sql1 = """SELECT
        0,
        card.card_name,
        card.id
        FROM
        card
        """
    cur = get_sql_done(sql1)
    lim = []
    for i in cur:
        lim.append(list(i))
    return lim


# 获取老师基本信息
def getteacherbasicinfo(request):
    serial = request.GET.get("serial")
    sql = f"""
    SELECT
        employee.`name`,
        employee.serial,
        SUBSTRING_INDEX( campus.campus_name, "（",1 ) campus_name,
        SUBSTR( campus.campus_name FROM - 6 FOR 5 ) campus_serial 
    FROM
        employee,
        campus 
    WHERE
        employee.campus_id = campus.campus_id 
        AND employee.serial =  '{serial}'
    """
    cur = get_sql_done(sql)
    for item in cur:
        li = item
    return list(li)


# 获取老师卡牌明细，返回一个三维列表
def getteachercard(quest):
    serial = quest.GET.get("serial")
    sql = f"""
    SELECT
    Count(student_card.card_num) AA,
    card.card_name,
    card_id
    FROM
    student_card ,
    card
    WHERE
    student_card.employee_id = (SELECT employee.employee_id FROM employee WHERE employee.serial = '{serial}') AND
    student_card.card_id = card.id
    GROUP BY
    student_card.card_id
    ORDER BY card_id DESC
    """
    cur = get_sql_done(sql)
    # 用于生成固定格式且固定长度的列表
    lii = getcardname()
    for item in cur:
        lii[item[2] - 1] = list(item)
    return lii


# 获取老师教授的班级
def getteacherclazz(quest) -> List:
    serial = quest.GET.get("serial")
    sql = f"""
    SELECT DISTINCT
    stu_class_current.class_id,
    stu_class.`name`,
    SUBSTR(stu_class.`name` FROM 4 FOR 7) num
    FROM
    stu_class_current ,
    student ,
    stu_class
    WHERE
    student.student_id = stu_class_current.student_id AND
    student.campus_id = LCASE((SELECT
    employee.campus_id
    FROM
    employee
    WHERE
    employee.serial = '{serial}')) AND
    stu_class_current.class_id = stu_class.class_id
    ORDER BY num"""
    cur = get_sql_done(sql)
    tlist = []
    for i in cur:
        tlist.append(list(i)[:2])
    print(type(tlist))
    return tlist


# 获取老师教授的课
def getteachercourse(quest) -> List:
    serial = quest.GET.get("serial")
    sql = f"""
    SELECT DISTINCT
    course_extra.course_id,
    course_extra.course_name
    FROM
    student_card ,
    course_extra
    WHERE
    student_card.course_id = course_extra.course_id AND
    student_card.employee_id = ( SELECT employee.employee_id FROM employee WHERE employee.serial = ( '{serial}' ) )"""
    li = []
    cur = get_sql_done(sql)
    for i in cur:
        li.append(list(i))
    cname = []

    for ite in li:
        if ite[1] not in cname:
            cname.append(ite[1])
    return cname
