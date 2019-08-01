import json
from random import randrange

from django.http import HttpResponse
from example.commons import Faker
from rest_framework.views import APIView

from pyecharts.charts import Bar
from pyecharts import options as opts


# Create your views here.
from StudentInfo.DataBaseUtilsStudent import get5sumbase


def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def bar_base() -> Bar:
    c = (
        Bar()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values(), stack="stack1")
            .add_yaxis("商家B", Faker.values(), stack="stack1")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（部分）"))
            .dump_options()
    )
    # c = (
    #     Bar()
    #     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    #     .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
    #     .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
    #     .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    #     .dump_options()
    # )
    return c


class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base()))

class Card2View(APIView):
    def get(self,request,*args,**kwargs):
        cur = get5sumbase('S00494')
        li = []
        for i in cur:
            li = i
        print(li)
        return JsonResponse(li)



class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/index.html", encoding='utf8').read())


def campus_cat_sum_cnt():
    pass


def class_cat_sum_cnt():
    pass


def cat_sum_cnt():
    return None


def cat_national_sum_rank():
    return None
