from django.http import HttpResponse
from rest_framework.views import APIView
from TeacherInfo.doteacherquery import getteacherbasicinfo, getteachercard, getteacherclazz, getteachercourse
from utils.jsonutil import json_response, json_error

JsonResponse = json_response
JsonError = json_error


class BasicInfo(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(getteacherbasicinfo(request))


class AllCard(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(getteachercard(request))


class AllClazz(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(getteacherclazz(request))


class AllCourse(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(getteachercourse(request))


class Teacher(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/teacher.html", encoding='utf8').read())
