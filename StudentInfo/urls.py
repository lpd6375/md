from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cat_sum_cnt/$', views.cat_sum_cnt, name='StudentInfo'),
    url(r'^cat_national_sum_rank/$', views.cat_national_sum_rank, name='StudentInfo'),
    url(r'^class_cat_sum_cnt/$', views.class_cat_sum_cnt, name='StudentInfo'),
    url(r'^campus_cat_sum_cnt/$', views.campus_cat_sum_cnt, name='StudentInfo'),
    # url(r'^cat_cnt/$', views.cat_cnt, name='StudentInfo'),
    # url(r'^cat_cnt/$', views.cat_cnt, name='StudentInfo'),
    # url(r'^cat_cnt/$', views.cat_cnt, name='StudentInfo'),

]
