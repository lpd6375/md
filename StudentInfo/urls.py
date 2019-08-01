from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='StudentInfo'),
    url(r'^cat_sum_cnt/$', views.Card2View.as_view(), name='StudentInfo'),
    url(r'^cat_national_sum_rank/$', views.NationRank.as_view(), name='StudentInfo'),
    url(r'^class_cat_sum_cnt/$', views.ClassRank.as_view(), name='StudentInfo'),
    url(r'^campus_cat_sum_cnt/$', views.CampusRank.as_view(), name='StudentInfo'),
    url(r'^get_student_basic_info/$', views.BaseInfo.as_view(), name='StudentInfo'),

]
