from django.conf.urls import url

from OperationInfo import views

urlpatterns=[
    url(r'^getOperation',views.getoperationinfo,name='OperationInfo')
]