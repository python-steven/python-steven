from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,HttpResponse
from app.access_control import access_control
from django.db import connection
from app import restful,mail
from datetime import datetime,timedelta,date
from django.conf import settings
from openpyxl import load_workbook,Workbook
from django.db.models import Q,F
from .models import ProjectsName,Customers,BU,EquipmentVendor,EquipmentType,Station,QuestionClass,FAMode,EquipmentNumber
from app.login.models import LocationLog
import random,string,os,time,json,copy,traceback

@csrf_exempt
def GetProject(request):
    try:
        page = int(request.GET.get('page'))
        number =int(request.GET.get('num'))
        dict_data ={}
        sql = 'SELECT * FROM "ProjectsName"'
        sql2 = 'SELECT count(*) FROM "ProjectsName"'
        cur = connection.cursor()
        cur.execute(sql2)
        count = cur.fetchall()  # 数量的总数
        count_page = count[0][0]//number #总页数
        if count[0][0]%number>0:
            count_page +=1
        if page <=count_page:
            sql =sql + ' order by "Id" desc limit ' + str(number) + ' offset ' + str((page - 1)*number)
            cur = connection.cursor()
            cur.execute(sql, None)
            desc = cur.description
            data = [dict(zip([col[0] for col in desc], row)) for row in cur.fetchall()]
            dict_data['data']=data
            dict_data['total_count']=count
            dict_data['page_current']=page
            dict_data['page_count']=count_page
            return restful.ok(data=dict_data)
        else:
            return restful.params_error(message="no had other pages")
    except:
        return restful.params_error(message=traceback.format_exc())
# add Project function
@csrf_exempt
def AddProject(request):
    try:
        Name = request.POST.get("Name")
        UpdatedTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if Name and len(list(ProjectsName.objects.filter(Name=Name).values())) ==0:
            ProjectsName.objects.create(Name=Name,UpdatedTime=UpdatedTime)
            return restful.ok(message="create Project Name successful")
        else:
            return restful.params_error(message="projects Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())
# modify projects function
@csrf_exempt
def ModifyProject(request):
    try:
        Id = request.POST.get("Id")
        Name = request.POST.get("Name")
        if Name:
            ProjectsName.objects.filter(Id=Id).update(Name=Name)
            return restful.ok(message="Modify Project Name successful")
        else:
            return restful.params_error(message="projects Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())
# delete projects function
@csrf_exempt
def DeleteProject(request):
    try:
        Id = request.POST.get("Id")
        if Id:
            ProjectsName.objects.filter(Id=Id).delete()
            return restful.ok(message="Delete Project Name successful")
        else:
            return restful.params_error(message="projects Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())


# get Customer info
@csrf_exempt
def GetCustmoers(request):
    try:
        page = int(request.GET.get('page'))
        number =int(request.GET.get('num'))
        dict_data ={}
        sql = 'SELECT * FROM "Customers"'
        sql2 = 'SELECT count(*) FROM "Customers"'
        cur = connection.cursor()
        cur.execute(sql2)
        count = cur.fetchall()  # 数量的总数
        count_page = count[0][0]//number #总页数
        if count[0][0]%number>0:
            count_page +=1
        if page <=count_page:
            sql =sql + ' order by "Id" desc limit ' + str(number) + ' offset ' + str((page - 1)*number)
            cur = connection.cursor()
            cur.execute(sql, None)
            desc = cur.description
            data = [dict(zip([col[0] for col in desc], row)) for row in cur.fetchall()]
            dict_data['data']=data
            dict_data['total_count']=count
            dict_data['page_current']=page
            dict_data['page_count']=count_page
            return restful.ok(data=dict_data)
        else:
            return restful.params_error(message="no had other pages")
    except:
        return restful.params_error(message=traceback.format_exc())
# add Customer function
@csrf_exempt
def AddCustomer(request):
    try:
        Name = request.POST.get("Name")
        UpdatedTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if Name and len(list(Customers.objects.filter(Name=Name).values())) ==0:
            Customers.objects.create(Name=Name,UpdatedTime=UpdatedTime)
            return restful.ok(message="create Customers Name successful")
        else:
            return restful.params_error(message="projects Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#modify
@csrf_exempt
def ModifyCustomer(request):
    try:
        Id = request.POST.get("Id")
        Name = request.POST.get("Name")
        if Name:
            Customers.objects.filter(Id=Id).update(Name=Name)
            return restful.ok(message="Modify Customers Name successful")
        else:
            return restful.params_error(message="Modify Customers Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#del
@csrf_exempt
def DeleteCustomer(request):
    try:
        Id = request.POST.get("Id")
        if Id:
            Customers.objects.filter(Id=Id).delete()
            return restful.ok(message="Delete Customers Name successful")
        else:
            return restful.params_error(message="Customers Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())


# BU get
@csrf_exempt
def GetBUs(request):
    try:
        page = int(request.GET.get('page'))
        number =int(request.GET.get('num'))
        dict_data ={}
        sql = 'SELECT * FROM "BU"'
        sql2 = 'SELECT count(*) FROM "BU"'
        cur = connection.cursor()
        cur.execute(sql2)
        count = cur.fetchall()  # 数量的总数
        count_page = count[0][0]//number #总页数
        if count[0][0]%number>0:
            count_page +=1
        if page <=count_page:
            sql =sql + ' order by "Id" desc limit ' + str(number) + ' offset ' + str((page - 1)*number)
            cur = connection.cursor()
            cur.execute(sql, None)
            desc = cur.description
            data = [dict(zip([col[0] for col in desc], row)) for row in cur.fetchall()]
            dict_data['data']=data
            dict_data['total_count']=count
            dict_data['page_current']=page
            dict_data['page_count']=count_page
            return restful.ok(data=dict_data)
        else:
            return restful.params_error(message="no had other pages")
    except:
        return restful.params_error(message=traceback.format_exc())
# add BU function
@csrf_exempt
def AddBUs(request):
    try:
        BUName = request.POST.get("Name")
        UpdatedTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if BUName and len(list(BU.objects.filter(BUName=BUName).values())) ==0:
            BU.objects.create(BUName=BUName,UpdatedTime=UpdatedTime)
            return restful.ok(message="create BU Name successful")
        else:
            return restful.params_error(message="BU Name had exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#modify
@csrf_exempt
def ModifyBU(request):
    try:
        Id = request.POST.get("Id")
        BUName = request.POST.get("Name")
        if BUName:
            BU.objects.filter(Id=Id).update(BUName=BUName)
            return restful.ok(message="Modify BU Name successful")
        else:
            return restful.params_error(message="BU Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#del
@csrf_exempt
def DeleteBU(request):
    try:
        Id = request.POST.get("Id")
        if Id:
            BU.objects.filter(Id=Id).delete()
            return restful.ok(message="Delete BU Name successful")
        else:
            return restful.params_error(message="BU Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())


# vendor get
@csrf_exempt
def GetVendors(request):
    try:
        page = int(request.GET.get('page'))
        number =int(request.GET.get('num'))
        dict_data ={}
        sql = 'SELECT * FROM "EquipmentVendor"'
        sql2 = 'SELECT count(*) FROM "EquipmentVendor"'
        cur = connection.cursor()
        cur.execute(sql2)
        count = cur.fetchall()  # 数量的总数
        count_page = count[0][0]//number #总页数
        if count[0][0]%number>0:
            count_page +=1
        if page <=count_page:
            sql =sql + ' order by "Id" desc limit ' + str(number) + ' offset ' + str((page - 1)*number)
            cur = connection.cursor()
            cur.execute(sql, None)
            desc = cur.description
            data = [dict(zip([col[0] for col in desc], row)) for row in cur.fetchall()]
            dict_data['data']=data
            dict_data['total_count']=count
            dict_data['page_current']=page
            dict_data['page_count']=count_page
            return restful.ok(data=dict_data)
        else:
            return restful.params_error(message="no had other pages")
    except:
        return restful.params_error(message=traceback.format_exc())
# add vendor function
@csrf_exempt
def AddVendor(request):
    try:
        Vendor = request.POST.get("Name")
        UpdatedTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if Vendor and len(list(EquipmentVendor.objects.filter(Vendor=Vendor).values())) ==0:
            EquipmentVendor.objects.create(Vendor=Vendor,UpdatedTime=UpdatedTime)
            return restful.ok(message="create EquipmentVendor Name successful")
        else:
            return restful.params_error(message="EquipmentVendor Name had exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#modify
@csrf_exempt
def ModifyVendor(request):
    try:
        Id = request.POST.get("Id")
        Vendor = request.POST.get("Name")
        if Vendor:
            EquipmentVendor.objects.filter(Id=Id).update(Vendor=Vendor)
            return restful.ok(message="Modify EquipmentVendor Name successful")
        else:
            return restful.params_error(message="EquipmentVendor Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#del
@csrf_exempt
def DeleteVendor(request):
    try:
        Id = request.POST.get("Id")
        if Id:
            EquipmentVendor.objects.filter(Id=Id).delete()
            return restful.ok(message="Delete EquipmentVendor Name successful")
        else:
            return restful.params_error(message="EquipmentVendor Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())


# type get
@csrf_exempt
def GetTypes(request):
    try:
        page = int(request.GET.get('page'))
        number =int(request.GET.get('num'))
        dict_data ={}
        sql = 'SELECT * FROM "EquipmentType"'
        sql2 = 'SELECT count(*) FROM "EquipmentType"'
        cur = connection.cursor()
        cur.execute(sql2)
        count = cur.fetchall()  # 数量的总数
        count_page = count[0][0]//number #总页数
        if count[0][0]%number>0:
            count_page +=1
        if page <=count_page:
            sql =sql + ' order by "Id" desc limit ' + str(number) + ' offset ' + str((page - 1)*number)
            cur = connection.cursor()
            cur.execute(sql, None)
            desc = cur.description
            data = [dict(zip([col[0] for col in desc], row)) for row in cur.fetchall()]
            dict_data['data']=data
            dict_data['total_count']=count
            dict_data['page_current']=page
            dict_data['page_count']=count_page
            return restful.ok(data=dict_data)
        else:
            return restful.params_error(message="no had other pages")
    except:
        return restful.params_error(message=traceback.format_exc())
# add type function
@csrf_exempt
def AddType(request):
    try:
        Type = request.POST.get("Name")
        UpdatedTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if Type and len(list(EquipmentType.objects.filter(Type=Type).values())) ==0:
            EquipmentType.objects.create(Type=Type,UpdatedTime=UpdatedTime)
            return restful.ok(message="create EquipmentType Name successful")
        else:
            return restful.params_error(message="EquipmentType Name had exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#modify
@csrf_exempt
def ModifyType(request):
    try:
        Id = request.POST.get("Id")
        Type = request.POST.get("Name")
        if Type:
            EquipmentType.objects.filter(Id=Id).update(Type=Type)
            return restful.ok(message="Modify EquipmentType Name successful")
        else:
            return restful.params_error(message="EquipmentType Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#del
@csrf_exempt
def DeleteType(request):
    try:
        Id = request.POST.get("Id")
        if Id:
            EquipmentType.objects.filter(Id=Id).delete()
            return restful.ok(message="Delete EquipmentType Name successful")
        else:
            return restful.params_error(message="EquipmentType Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())


# type get
@csrf_exempt
def GetStations(request):
    try:
        page = int(request.GET.get('page'))
        number =int(request.GET.get('num'))
        dict_data ={}
        sql = 'SELECT * FROM "Station"'
        sql2 = 'SELECT count(*) FROM "Station"'
        cur = connection.cursor()
        cur.execute(sql2)
        count = cur.fetchall()  # 数量的总数
        count_page = count[0][0]//number #总页数
        if count[0][0]%number>0:
            count_page +=1
        if page <=count_page:
            sql =sql + ' order by "Id" desc limit ' + str(number) + ' offset ' + str((page - 1)*number)
            cur = connection.cursor()
            cur.execute(sql, None)
            desc = cur.description
            data = [dict(zip([col[0] for col in desc], row)) for row in cur.fetchall()]
            dict_data['data']=data
            dict_data['total_count']=count
            dict_data['page_current']=page
            dict_data['page_count']=count_page
            return restful.ok(data=dict_data)
        else:
            return restful.params_error(message="no had other pages")
    except:
        return restful.params_error(message=traceback.format_exc())
# add type function
@csrf_exempt
def AddStation(request):
    try:
        StationLine = request.POST.get("Name")
        UpdatedTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if StationLine and len(list(Station.objects.filter(StationLine=StationLine).values())) ==0:
            Station.objects.create(StationLine=StationLine,UpdatedTime=UpdatedTime)
            return restful.ok(message="create EquipmentType Name successful")
        else:
            return restful.params_error(message="EquipmentType Name had exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#modify
@csrf_exempt
def ModifyStation(request):
    try:
        Id = request.POST.get("Id")
        StationLine = request.POST.get("Name")
        if StationLine:
            Station.objects.filter(Id=Id).update(StationLine=StationLine)
            return restful.ok(message="Modify EquipmentType Name successful")
        else:
            return restful.params_error(message="EquipmentType Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#del
@csrf_exempt
def DeleteStation(request):
    try:
        Id = request.POST.get("Id")
        if Id:
            Station.objects.filter(Id=Id).delete()
            return restful.ok(message="Delete EquipmentType Name successful")
        else:
            return restful.params_error(message="EquipmentType Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())


# type get
@csrf_exempt
def GetQuestions(request):
    try:
        page = int(request.GET.get('page'))
        number =int(request.GET.get('num'))
        dict_data ={}
        sql = 'SELECT * FROM "QuestionClass"'
        sql2 = 'SELECT count(*) FROM "QuestionClass"'
        cur = connection.cursor()
        cur.execute(sql2)
        count = cur.fetchall()  # 数量的总数
        count_page = count[0][0]//number #总页数
        if count[0][0]%number>0:
            count_page +=1
        if page <=count_page:
            sql =sql + ' order by "Id" desc limit ' + str(number) + ' offset ' + str((page - 1)*number)
            cur = connection.cursor()
            cur.execute(sql, None)
            desc = cur.description
            data = [dict(zip([col[0] for col in desc], row)) for row in cur.fetchall()]
            dict_data['data']=data
            dict_data['total_count']=count
            dict_data['page_current']=page
            dict_data['page_count']=count_page
            return restful.ok(data=dict_data)
        else:
            return restful.params_error(message="no had other pages")
    except:
        return restful.params_error(message=traceback.format_exc())
# add type function
@csrf_exempt
def AddQuestion(request):
    try:
        Classify = request.POST.get("Name")
        UpdatedTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if Classify and len(list(QuestionClass.objects.filter(Classify=Classify).values())) ==0:
            QuestionClass.objects.create(Classify=Classify,UpdatedTime=UpdatedTime)
            return restful.ok(message="create Question Name successful")
        else:
            return restful.params_error(message="Question Name had exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#modify
@csrf_exempt
def ModifyQuestion(request):
    try:
        Id = request.POST.get("Id")
        Classify = request.POST.get("Name")
        if Classify:
            QuestionClass.objects.filter(Id=Id).update(Classify=Classify)
            return restful.ok(message="Modify Question Name successful")
        else:
            return restful.params_error(message="Question Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())
#del
@csrf_exempt
def DeleteQuestion(request):
    try:
        Id = request.POST.get("Id")
        if Id:
            QuestionClass.objects.filter(Id=Id).delete()
            return restful.ok(message="Delete Question Name successful")
        else:
            return restful.params_error(message="Question Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())


#get INfo
@csrf_exempt
def GETInfo(request):
    try:
        dict_data ={}
        dict_data["projects"] = list(ProjectsName.objects.all().values("Name"))
        dict_data['customers'] = list(Customers.objects.all().values("Name"))
        dict_data['bus'] = list(BU.objects.all().values("BUName"))
        dict_data['vendors'] = list(EquipmentVendor.objects.all().values("Vendor"))
        dict_data['types'] = list(EquipmentType.objects.all().values("Type"))
        dict_data['stations'] = list(Station.objects.all().values("StationLine"))
        dict_data['question'] = list(QuestionClass.objects.all().values("Classify"))
        return restful.ok(data=dict_data)
    except:
        return restful.params_error(message=traceback.format_exc())
#add Equipmentmanage
@csrf_exempt
def AddEquipmentManager(request):
    try:
        EquipmentNo = request.POST.get("NO")
        ProjectName = request.POST.get("project")
        Customer = request.POST.get("customer")
        BringToBU = request.POST.get("BU")
        EquipmentVendor = request.POST.get("vendor")
        EquipmentType = request.POST.get("type")
        StationLine = request.POST.get("station")
        if EquipmentNo and len(list(EquipmentNumber.objects.filter(EquipmentNo=EquipmentNo).values()))==0:
            EquipmentNumber.objects.create(EquipmentNo=EquipmentNo,ProjectName=ProjectName,Customer=Customer
                                           ,BringToBU=BringToBU,EquipmentVendor=EquipmentVendor
                                           ,EquipmentType=EquipmentType,StationLine=StationLine
                                           )
            return restful.ok(message="create Equipment manager successful")
        else:
            return restful.params_error(message=EquipmentNo+" had exist.")
    except:
        return restful.params_error(message=traceback.format_exc())

def GetEquipmentManager(request):
    try:
        page = int(request.GET.get('page'))
        number =int(request.GET.get('num'))
        dict_data ={}
        sql = 'SELECT * FROM "EquipmentNumber"'
        sql2 = 'SELECT count(*) FROM "EquipmentNumber"'
        cur = connection.cursor()
        cur.execute(sql2)
        count = cur.fetchall()  # 数量的总数
        count_page = count[0][0]//number #总页数
        if count[0][0]%number>0:
            count_page +=1
        if page <=count_page:
            sql =sql + ' order by "Id" desc limit ' + str(number) + ' offset ' + str((page - 1)*number)
            cur = connection.cursor()
            cur.execute(sql, None)
            desc = cur.description
            data = [dict(zip([col[0] for col in desc], row)) for row in cur.fetchall()]
            dict_data['data']=data
            dict_data['total_count']=count[0][0]
            dict_data['page_current']=page
            dict_data['page_count']=count_page
            return restful.ok(data=dict_data)
        else:
            return restful.params_error(message="no had other pages")
    except:
        return restful.params_error(message=traceback.format_exc())

@csrf_exempt
def ModifyEquipmentManager(request):
    try:
        Id = request.POST.get("Id")
        ProjectName = request.POST.get("project")
        Customer = request.POST.get("customer")
        BringToBU = request.POST.get("BU")
        EquipmentVendor = request.POST.get("vendor")
        EquipmentType = request.POST.get("type")
        StationLine = request.POST.get("station")
        if Id:
            EquipmentNumber.objects.filter(Id=Id).update(ProjectName=ProjectName,Customer=Customer
                                           ,BringToBU=BringToBU,EquipmentVendor=EquipmentVendor
                                           ,EquipmentType=EquipmentType,StationLine=StationLine
                                           )
            return restful.ok(message="update Equipment manager successful")
        else:
            return restful.params_error(message=" update number error.")
    except:
        return restful.params_error(message=traceback.format_exc())

@csrf_exempt
def DeleteEquipmentManager(request):
    try:
        Id = request.POST.get("Id")
        if Id:
            EquipmentNumber.objects.filter(Id=Id).delete()
            return restful.ok(message="Delete EquipmentNumber Name successful")
        else:
            return restful.params_error(message="EquipmentNumber Name not exist")
    except:
        return restful.params_error(message=traceback.format_exc())


@csrf_exempt
def GETFTINFO(request):
    try:
        dict_data ={}
        dict_data["NO"] = list(EquipmentNumber.objects.all().values("EquipmentNo"))
        dict_data['Station'] = list(Station.objects.all().values("StationLine"))
        dict_data['QuestionClass'] = list(QuestionClass.objects.all().values("Classify"))
        dict_data['lines'] = list(LocationLog.objects.all().values("Location"))
        return restful.ok(data=dict_data)
    except:
        return restful.params_error(message=traceback.format_exc())

@csrf_exempt
def AddFT(request):
    try:
        No = request.POST.get('NO')
        line = request.POST.get('line')
        Station = request.POST.get('Station')
        Q_type = request.POST.get('Q_type')
        Q_date = request.POST.get('Q_date')
        R_time = request.POST.get('R_time')
        A_Person = request.POST.get('A_Person')
        Q_desc = request.POST.get('Q_desc')
        Q_ess = request.POST.get('Q_ess')
        R_way = request.POST.get('R_way')
        R_mark = request.POST.get('R_mark')
        UpdatedTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        time_num = int(time.time())
        time_num = str(time_num)
        file = request.FILES.get('upload_file')  # 附件的获取
        if file:
            file_name = file.name
            file_sp_name = file_name.split('.')[0]
            file_ven_name = file_sp_name + time_num + '.' + file_name.split('.')[1]
            file_path = os.path.join(settings.MEDIA_ROOT, file_ven_name)
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            f.close()
            file_url = request.build_absolute_uri(settings.MEDIA_URL + file_ven_name)
        else:
            file_url = ""
        if No:
            FAMode.objects.create(EquipmentNo=No,Line=line,StationLine=Station
                                  ,QuestionDesc=Q_desc,EssentialIssues=Q_ess
                                  ,Solution=R_way,RepairTime=R_time,QuestionClassify=Q_type
                                  ,QuestionDate=Q_date,Analyst=A_Person,Remark=R_mark
                                  ,AttachmentPath=file_url,UpdatedTime=UpdatedTime)
        return restful.ok(message="create FT issue successful")
    except:
        return restful.params_error(message=traceback.format_exc())

def GETFAModes(request):
    try:
        page = int(request.GET.get('page'))
        number =int(request.GET.get('num'))
        dict_data ={}
        sql = 'SELECT "FAMode"."Id","FAMode"."QuestionDate","FAMode"."EquipmentNo","EquipmentNumber"."ProjectName","EquipmentNumber"."Customer"' \
              ',"EquipmentNumber"."BringToBU","EquipmentNumber"."EquipmentVendor","EquipmentNumber"."EquipmentType"' \
              ',"FAMode"."Line","EquipmentNumber"."StationLine" ,"FAMode"."QuestionDesc","FAMode"."EssentialIssues"' \
              ',"FAMode"."Solution","FAMode"."RepairTime","FAMode"."QuestionClassify","FAMode"."Analyst","FAMode"."AttachmentPath","FAMode"."Remark"' \
              ' FROM "FAMode" LEFT OUTER join "EquipmentNumber" ON "FAMode"."EquipmentNo" = "EquipmentNumber"."EquipmentNo"  '
        sql2 = 'SELECT count(*) FROM "FAMode" LEFT OUTER join "EquipmentNumber" ON "FAMode"."EquipmentNo" = "EquipmentNumber"."EquipmentNo"'
        cur = connection.cursor()
        cur.execute(sql2)
        count = cur.fetchall()  # 数量的总数
        count_page = count[0][0]//number #总页数
        if count[0][0]%number>0:
            count_page +=1
        if page <=count_page:
            sql =sql + ' order by "Id" desc limit ' + str(number) + ' offset ' + str((page - 1)*number)
            cur = connection.cursor()
            cur.execute(sql, None)
            desc = cur.description
            data = [dict(zip([col[0] for col in desc], row)) for row in cur.fetchall()]
            dict_data['data']=data
            dict_data['total_count']=count[0][0]
            dict_data['page_current']=page
            dict_data['page_count']=count_page
            return restful.ok(data=dict_data)
        else:
            return restful.params_error(message="no had other pages")
    except:
        return restful.params_error(message=traceback.format_exc())

def DeleteFT(request):
    try:
        Id = request.POST.get("Id")
        if Id:
            FAMode.objects.filter(Id=Id).delete()
            return restful.ok(message="Delete question issue successful")
        else:
            return restful.params_error(message="question issue not exist")
    except:
        return restful.params_error(message=traceback.format_exc())

@csrf_exempt
def ModifyFT(request):
    try:
        update_dict = {}
        Id = request.POST.get("Id")
        update_dict['EquipmentNo'] = request.POST.get('NO')
        update_dict['Line'] = request.POST.get('line')
        update_dict['StationLine'] = request.POST.get('Station')
        update_dict['QuestionClassify'] = request.POST.get('Q_type')
        update_dict['QuestionDate'] = request.POST.get('Q_date')
        update_dict['RepairTime'] = request.POST.get('R_time')
        update_dict['Analyst'] = request.POST.get('A_Person')
        update_dict['QuestionDesc'] = request.POST.get('Q_desc')
        update_dict['EssentialIssues'] = request.POST.get('Q_ess')
        update_dict['Solution'] = request.POST.get('R_way')
        update_dict['Remark'] = request.POST.get('R_mark')
        update_dict['UpdatedTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')



        time_num = int(time.time())
        time_num = str(time_num)
        file = request.FILES.get('upload_file')  # 附件的获取
        if file:
            file_name = file.name
            file_sp_name = file_name.split('.')[0]
            file_ven_name = file_sp_name + time_num + '.' + file_name.split('.')[1]
            file_path = os.path.join(settings.MEDIA_ROOT, file_ven_name)
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            f.close()
            file_url = request.build_absolute_uri(settings.MEDIA_URL + file_ven_name)
        else:
            file_url = ""
        if file_url != "":
            update_dict['AttachmentPath']=file_url

        if Id:
            FAMode.objects.filter(Id=Id).update(**update_dict)
            return restful.ok(message="update FT issue successful")

        else:
            return restful.params_error(message=" update number error.")
    except:
        return restful.params_error(message=traceback.format_exc())

@csrf_exempt
def GETQueryInfo(request):
    try:
        dict_data = {}
        dict_data["NO"] = list(EquipmentNumber.objects.all().values("EquipmentNo"))
        dict_data['QuestionClass'] = list(QuestionClass.objects.all().values("Classify"))
        dict_data['ProjectsName'] = list(ProjectsName.objects.all().values("Name"))
        dict_data['Customers'] = list(Customers.objects.all().values("Name"))
        dict_data['EquipmentVendor'] = list(EquipmentVendor.objects.all().values("Vendor"))
        dict_data['EquipmentType'] = list(EquipmentType.objects.all().values("Type"))
        return restful.ok(data=dict_data)
    except:
        return restful.params_error(message=traceback.format_exc())