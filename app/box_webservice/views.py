#-*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
# import logging
# logging.basicConfig(level=logging.DEBUG)
#from spyne import Application, rpc, ServiceBase,Integer, Unicode
from spyne import Application,rpc,ServiceBase,Iterable,Integer,Unicode
from spyne.model.primitive import String, Unicode, Boolean, DateTime, Int
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne import Iterable
from spyne.protocol.xml import XmlDocument
from spyne.protocol.json import JsonDocument
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt
from app.BoxID.models import Box,SerialNumberInfo,ModelStage
import json
from app import restful,mail
from django.db.models import Q,F

class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=String)
    def QueryLinkSN(ctx, post_data):
        check_box = list(Box.objects.filter(BoxId=post_data).values("Id"))
        if len(check_box) != 0:
            countt = ModelStage.objects.filter(ModelStage=check_box[0]["ModelStageId"]).values_list("RequireQuantity",flat=True)
            qty = 0
            for i in countt:
                qty +=i

            data1 = []
            data_SN = list(
                SerialNumberInfo.objects.filter(BoxIdBindingId=int(check_box[0]["Id"])).values_list("SerialNumber"))

            for i in data_SN:
                data1.append(i[0])
            if len(data1) ==qty:
             return str(data1)
            else:
                return "Box had't binding finished"
        else:
            return "Query NO data"

    @rpc(Unicode, _returns=String)
    def QueryAllSN(ctx, post_data):
        check_box = list(Box.objects.filter(BoxId=post_data).values("Id"))
        if len(check_box) != 0:
            data_SN = list(SerialNumberInfo.objects.filter(BoxIdBindingId=int(check_box[0]["Id"])).values("SerialNumber","PartCode"))
            countt = ModelStage.objects.filter(ModelStage=check_box[0]["ModelStageId"]).values_list("RequireQuantity",flat=True)
            qty = 0
            for i in countt:
                qty += i
            for i in data_SN:
                if len(list(ModelStage.objects.filter(~Q(BrushNumber=0)&(Q(PartCode=i["PartCode"])|Q(AlternativePartCode__contains=i["PartCode"]))).values("PartName"))) !=0:
                    i["PartName"] =list(ModelStage.objects.filter(PartCode=i["PartCode"]).values("PartName"))[0]["PartName"]
                else:
                    i["PartName"]=""
            if len(data_SN) == qty:
                return str(data_SN)
            else:
                return "Box had't binding finished"
        else:
            return "Query NO data"
#
application = Application([HelloWorldService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
# # This module resides in a package in your Django
information_app = csrf_exempt(DjangoApplication(application))

def Information_Box(request):
    try:
        box_item = request.GET.get("box",'')
        check_box = list(Box.objects.filter(BoxId=box_item).values("Id"))
        if len(check_box) !=0:
            data =[]
            data_SN = list(SerialNumberInfo.objects.filter(BoxIdBindingId=int(check_box[0]["Id"])).values_list("SerialNumber"))
            for i in data_SN:
                data.append(i[0])
            return HttpResponse(json.dumps(data,ensure_ascii=False),content_type="application/json,charset=utf-8")
        else:
            return restful.params_error(message="NO data",data=box_item)
    except Exception as e:
        return restful.params_error(message=e)

