import json
from django.http import HttpResponse
from rest_framework.views import APIView
from StudentInfo.DataBaseUtilsStudent import get5sumbase, get_student_basic_info, getcatenationrank, getclassrank, \
    getcampusrank
from utils.jsonutil import json_response, json_error

JsonResponse = json_response
JsonError = json_error
# def bar_base() -> Bar:
#     c = (
#         Bar()
#             .add_xaxis(Faker.choose())
#             .add_yaxis("商家A", Faker.values(), stack="stack1")
#             .add_yaxis("商家B", Faker.values(), stack="stack1")
#             .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#             .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（部分）"))
#             .dump_options()
#     )
#     return c
# class ChartView(APIView):
#     def get(self, request, *args, **kwargs):
#         return JsonResponse(json.loads(bar_base()))


class Card2View(APIView):
    def get(self, request, *args, **kwargs):
        cur = get5sumbase(request)
        li = []
        for i in cur:
            li = i
        print(li)
        return JsonResponse(li)


class BaseInfo(APIView):
    def get(self, request, *args, **kwargs):
        info = get_student_basic_info(request)
        return JsonResponse(info)


class NationRank(APIView):
    def get(self, request, *args, **kwargs):
        info = getcatenationrank(request)
        return JsonResponse(info)


class ClassRank(APIView):
    def get(self, request, *args, **kwargs):
        info = getclassrank(request)
        return JsonResponse(info)


class CampusRank(APIView):
    def get(self, request, *args, **kwargs):
            info = getcampusrank(request)
            return JsonResponse(info)


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/student.html", encoding='utf8').read())
