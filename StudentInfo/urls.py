from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='StudentInfo'),
    url(r'^cat_sum_cnt/$', views.Card2View.as_view(), name='StudentInfo'),
    url(r'^cat_national_sum_rank/$', views.cat_national_sum_rank, name='StudentInfo'),
    url(r'^class_cat_sum_cnt/$', views.class_cat_sum_cnt, name='StudentInfo'),
    url(r'^campus_cat_sum_cnt/$', views.campus_cat_sum_cnt, name='StudentInfo'),

]
