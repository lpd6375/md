# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AchievementPd(models.Model):
    ac_id = models.AutoField(primary_key=True)
    pd_theme_id = models.IntegerField()
    ac_img = models.CharField(max_length=255)
    ac_name = models.CharField(max_length=255)
    ac_describe = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'achievement_pd'


class AchievementPdGroup(models.Model):
    ac_id = models.AutoField(primary_key=True)
    ac_img = models.CharField(max_length=255)
    ac_name = models.CharField(max_length=255)
    ac_describe = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'achievement_pd_group'
        unique_together = (('ac_id', 'ac_describe'),)


class BasicCourseCard(models.Model):
    basic_course_extra_id = models.IntegerField(primary_key=True)
    card_id = models.IntegerField()
    total_card_number = models.PositiveIntegerField(blank=True, null=True)
    card_number = models.CharField(max_length=10, blank=True, null=True)
    invent_type = models.PositiveIntegerField()
    course_question = models.TextField()
    cindex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'basic_course_card'
        unique_together = (('basic_course_extra_id', 'card_id'),)


class BasicCourseCardPd(models.Model):
    basic_course_extra_pd_id = models.IntegerField(primary_key=True)
    card_id = models.IntegerField()
    total_card_number = models.PositiveIntegerField(blank=True, null=True)
    card_number = models.CharField(max_length=10, blank=True, null=True)
    invent_type = models.PositiveIntegerField()
    course_question = models.TextField()
    cindex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'basic_course_card_pd'
        unique_together = (('basic_course_extra_pd_id', 'card_id'),)


class BasicCourseExtra(models.Model):
    sort = models.PositiveIntegerField()
    class_level_id = models.PositiveIntegerField()
    mark = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    course_en_name = models.CharField(max_length=255)
    course_img = models.CharField(max_length=255)
    total_card_number = models.PositiveIntegerField()
    card_number = models.PositiveIntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basic_course_extra'
        unique_together = (('sort', 'class_level_id'),)


class BasicCourseExtraPd(models.Model):
    sort = models.PositiveIntegerField()
    course_name = models.CharField(max_length=255)
    course_en_name = models.CharField(max_length=255)
    course_img = models.CharField(max_length=255)
    total_card_number = models.PositiveIntegerField()
    card_number = models.PositiveIntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    is_last_one = models.PositiveIntegerField()
    pd_theme_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'basic_course_extra_pd'
        unique_together = (('sort', 'pd_theme_id'),)


class BasicPdTheme(models.Model):
    status = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    campus = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sub_theme_number = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'basic_pd_theme'


class Campus(models.Model):
    campus_id = models.CharField(primary_key=True, max_length=36)
    campus_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'campus'


class Card(models.Model):
    card_name = models.CharField(max_length=255)
    card_en_name = models.CharField(max_length=255)
    card_img = models.CharField(max_length=255)
    card_cate_id = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card'


class CardCategory(models.Model):
    card_cate_name = models.CharField(max_length=200)
    card_cate_en_name = models.CharField(max_length=200)
    card_cate_img = models.CharField(max_length=255)
    sort_order = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'card_category'


class CardTag(models.Model):
    card_id = models.PositiveIntegerField()
    card_tag = models.CharField(max_length=255)
    card_tag_type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'card_tag'


class CardType(models.Model):
    card_type = models.CharField(max_length=255)
    default_number = models.CharField(max_length=255)
    is_del = models.IntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_type'


class ClassLevel(models.Model):
    class_level = models.CharField(unique=True, max_length=255)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    is_del = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'class_level'


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=36)
    campus_id = models.CharField(max_length=36)
    shift_id = models.CharField(max_length=36)
    class_id = models.CharField(max_length=36)
    user_id = models.CharField(max_length=36)
    user_id_help = models.CharField(max_length=36, blank=True, null=True)
    starttime = models.CharField(max_length=255)
    endtime = models.CharField(max_length=255)
    total_number = models.PositiveIntegerField()
    fact_number = models.PositiveIntegerField()
    course_status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'course'


class CourseCard(models.Model):
    course_id = models.CharField(max_length=36)
    card_id = models.IntegerField()
    total_card_number = models.PositiveIntegerField(blank=True, null=True)
    card_number = models.CharField(max_length=10, blank=True, null=True)
    invent_type = models.PositiveIntegerField()
    course_question = models.TextField()
    cindex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course_card'


class CourseExtra(models.Model):
    course_id = models.CharField(primary_key=True, max_length=36)
    course_name = models.CharField(max_length=255)
    course_en_name = models.CharField(max_length=255)
    course_img = models.CharField(max_length=255)
    total_card_number = models.PositiveIntegerField()
    card_number = models.PositiveIntegerField()
    course_type = models.IntegerField()
    basic_course_pd_id = models.IntegerField()
    basic_pd_theme_id = models.IntegerField()
    period = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'course_extra'


class CurrentPjps(models.Model):
    id = models.IntegerField(primary_key=True)
    next_basic_sort = models.IntegerField()
    is_stop = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    current_basic_sort = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    max_basic_sort = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_pjps'


class Employee(models.Model):
    employee_id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)
    campus_id = models.CharField(max_length=36, blank=True, null=True)
    serial = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    outdate = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeExtra(models.Model):
    employee_id = models.CharField(primary_key=True, max_length=36)
    account = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255, blank=True, null=True)
    token_expire_time = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    extra_auth = models.PositiveIntegerField()
    identify_date = models.DateField(blank=True, null=True)
    level = models.PositiveIntegerField()
    img = models.CharField(max_length=255, blank=True, null=True)
    real_name = models.CharField(max_length=255, blank=True, null=True)
    is_top = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_extra'


class EmployeeHonor(models.Model):
    employee_id = models.CharField(max_length=255)
    honor_id = models.IntegerField()
    reason = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.IntegerField()
    updated_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'employee_honor'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Honor(models.Model):
    name = models.CharField(unique=True, max_length=10)
    description = models.CharField(max_length=64)
    img = models.CharField(max_length=255)
    created = models.IntegerField()
    created_by = models.IntegerField()
    updated = models.IntegerField()
    updated_by = models.IntegerField()
    type = models.SmallIntegerField(blank=True, null=True)
    limit = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'honor'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=200)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Level(models.Model):
    name = models.CharField(unique=True, max_length=10)
    description = models.CharField(max_length=64)
    is_active = models.CharField(max_length=1)
    created = models.IntegerField()
    created_by = models.IntegerField()
    updated = models.IntegerField()
    updated_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'level'


class MessagePushLog(models.Model):
    eventkey = models.CharField(max_length=255)
    eventid = models.CharField(max_length=255)
    push_time = models.CharField(max_length=255)
    event_status = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    req_info = models.CharField(max_length=4096, blank=True, null=True)
    res_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_push_log'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class PermissionRole(models.Model):
    permission = models.ForeignKey('Permissions', models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'permission_role'
        unique_together = (('permission', 'role'),)


class Permissions(models.Model):
    name = models.CharField(unique=True, max_length=191)
    pid = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField()
    type = models.IntegerField()
    icon = models.CharField(max_length=30, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    method = models.CharField(max_length=50, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class ProjectAds(models.Model):
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    ad_pic = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    width = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    position_left = models.CharField(max_length=30)
    position_top = models.CharField(max_length=30)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_ads'


class Projects(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(unique=True, max_length=50)
    token = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    used_times = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projects'


class Regions(models.Model):
    id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    parent_id = models.IntegerField()
    short_name = models.CharField(max_length=20, blank=True, null=True)
    level = models.IntegerField()
    city_code = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    merger_name = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=30, blank=True, null=True)
    lat = models.CharField(max_length=30, blank=True, null=True)
    full_pinyin = models.CharField(max_length=255, blank=True, null=True)
    pinyin = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'


class RoleUser(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_user'
        unique_together = (('user', 'role'),)


class Roles(models.Model):
    name = models.CharField(unique=True, max_length=191)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Shift(models.Model):
    shift_id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shift'


class StuClass(models.Model):
    class_id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)
    campus_id = models.CharField(max_length=50, blank=True, null=True)
    isfinished = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stu_class'


class StuClassCurrent(models.Model):
    student_id = models.CharField(max_length=255)
    class_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stu_class_current'


class StuClassCurrentCopy(models.Model):
    student_id = models.CharField(max_length=255)
    class_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stu_class_current_copy'


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)
    headimgurl = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255)
    campus_id = models.CharField(max_length=36, blank=True, null=True)
    class_id = models.CharField(max_length=36, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    trystatus = models.SmallIntegerField(blank=True, null=True)
    trystatus_date = models.CharField(max_length=128, blank=True, null=True)
    is_exception_out = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentAbsence(models.Model):
    student_id = models.CharField(max_length=36)
    course_id = models.CharField(max_length=36)
    employee_id = models.CharField(max_length=36)
    name = models.CharField(max_length=255)
    cost = models.IntegerField(blank=True, null=True)
    istry = models.IntegerField(blank=True, null=True)
    isattend = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_absence'


class StudentAchievementPd(models.Model):
    ac_pd_id = models.PositiveIntegerField()
    student_id = models.CharField(max_length=36)
    employee_id = models.CharField(max_length=36)
    course_id = models.CharField(max_length=36)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    period = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_achievement_pd'


class StudentAchievementPdGroup(models.Model):
    ac_pd_group_id = models.PositiveIntegerField()
    student_id = models.CharField(max_length=36)
    employee_id = models.CharField(max_length=36)
    course_id = models.CharField(max_length=36)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    period = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_achievement_pd_group'


class StudentAchivement(models.Model):
    achivement_id = models.IntegerField(primary_key=True)
    imgurl1 = models.CharField(max_length=255)
    imgurl2 = models.CharField(max_length=255)
    imgurl3 = models.CharField(max_length=255)
    imgurl4 = models.CharField(max_length=255)
    imgurl5 = models.CharField(max_length=255)
    imgurltotal = models.CharField(max_length=255)
    imgurldescribe = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'student_achivement'


class StudentCard(models.Model):
    card_id = models.PositiveIntegerField()
    student_id = models.CharField(max_length=36)
    employee_id = models.CharField(max_length=36)
    course_id = models.CharField(max_length=36)
    card_num = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_card'


class StudentExtra(models.Model):
    student_id = models.CharField(primary_key=True, max_length=36)
    diy_headimgurl = models.CharField(max_length=255, blank=True, null=True)
    cate_one_number = models.PositiveIntegerField()
    cate_two_number = models.PositiveIntegerField()
    cate_three_number = models.PositiveIntegerField()
    cate_four_number = models.PositiveIntegerField()
    cate_five_number = models.PositiveIntegerField()
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=36, blank=True, null=True)
    token_expire_time = models.IntegerField(blank=True, null=True)
    passport_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_extra'


class SysConfig(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    type = models.CharField(max_length=8)
    value = models.TextField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    show_order = models.IntegerField()
    group = models.CharField(max_length=50)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_config'


class Test(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class UserChatLog(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    username = models.CharField(max_length=50)
    to_user_id = models.PositiveIntegerField()
    to_user_name = models.CharField(max_length=50)
    group_id = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_chat_log'


class UserPassports(models.Model):
    passport_id = models.AutoField(primary_key=True)
    openid = models.CharField(unique=True, max_length=30, blank=True, null=True)
    unionid = models.CharField(max_length=30, blank=True, null=True)
    groupid = models.IntegerField()
    nickname = models.CharField(max_length=50, blank=True, null=True)
    headimgurl = models.CharField(max_length=200, blank=True, null=True)
    sex = models.IntegerField()
    subscribe = models.IntegerField()
    phone = models.CharField(unique=True, max_length=11, blank=True, null=True)
    email = models.CharField(unique=True, max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    county = models.CharField(max_length=30, blank=True, null=True)
    subscribe_time = models.DateTimeField(blank=True, null=True)
    unsubscribe_time = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_passports'


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=70)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, blank=True, null=True)
    passport_id = models.IntegerField()
    score = models.IntegerField()
    score_total = models.IntegerField()
    chat_sign = models.CharField(max_length=100)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_super = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VerifyLog(models.Model):
    verify_text = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    code = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verify_log'
