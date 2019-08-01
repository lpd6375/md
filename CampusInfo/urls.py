from django.conf.urls import url

from CampusInfo import views

urlpatterns=[
    url(r'^getcampus',views.getcampusinfo,name='CampusInfo')
]