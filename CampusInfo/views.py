from django.http import HttpResponse
from rest_framework.views import APIView

from CampusInfo.campusquery import getcampusnsn, getcampusbasicinfo
from utils.jsonutil import json_response, json_error

JsonResponse = json_response
JsonError = json_error


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/campus.html", encoding='utf8').read())


class CampusView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(getcampusnsn())


class CampusInfoView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(getcampusbasicinfo(request))
