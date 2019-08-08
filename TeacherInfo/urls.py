from django.conf.urls import url

from TeacherInfo import views

urlpatterns = [
    url(r'^teacher/$', views.Teacher.as_view(), name='TeacherInfo'),
    url(r'^getbasicinfo/$', views.BasicInfo.as_view(), name='TeacherInfo'),
    url(r'^getaclz/$', views.AllClazz.as_view(), name='TeacherInfo'),
    url(r'^getcard/$', views.AllCard.as_view(), name='TeacherInfo'),
    url(r'^getcourse/$', views.AllCourse.as_view(), name='TeacherInfo'),

]




