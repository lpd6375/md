from django.conf.urls import url

from CampusInfo import views

urlpatterns = [
    url(r'^index', views.IndexView.as_view(), name='CampusInfo'),
    url(r'^getcampus', views.CampusView.as_view(), name='CampusInfo'),
    url(r'^getcampusinfo', views.CampusInfoView.as_view(), name='CampusInfo'),
]
