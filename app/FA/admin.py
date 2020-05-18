from django.contrib import admin
from .models import ProjectsName,Customers,BU,EquipmentVendor,EquipmentType,Station,QuestionClass,FAMode,EquipmentNumber
# Register your models here.

class ProjectsNameAdmin(admin.ModelAdmin):
    list_display = ('Id','Name','CreateTime','UpdatedTime')
    search_fields = ('Name',)
    ordering = ('Id',)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('Id','Name','CreateTime','UpdatedTime')
    search_fields = ('Name',)
    ordering = ('Id',)
class BUAdmin(admin.ModelAdmin):
    list_display = ('Id','BUName','CreateTime','UpdatedTime')
    search_fields = ('BUName',)
    ordering = ('Id',)

class EquipmentVendorAdmin(admin.ModelAdmin):
    list_display = ('Id','Vendor','CreateTime','UpdatedTime')
    search_fields = ('Vendor',)
    ordering = ('Id',)

class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('Id','Type','CreateTime','UpdatedTime')
    search_fields = ('Type',)
    ordering = ('Id',)

class StationAdmin(admin.ModelAdmin):
    list_display = ('Id','StationLine','CreateTime','UpdatedTime')
    search_fields = ('StationLine',)
    ordering = ('Id',)

class QuestionClassAdmin(admin.ModelAdmin):
    list_display = ('Id','Classify','CreateTime','UpdatedTime')
    search_fields = ('Classify',)
    ordering = ('Id',)

class EquipmentNumberAdmin(admin.ModelAdmin):
    list_display = ('Id','EquipmentNo','ProjectName','Customer','BringToBU'
                    ,'EquipmentVendor','EquipmentType','StationLine','CreateTime'
                    ,'UpdatedTime')
    search_fields = ('EquipmentNo',)
    ordering = ('Id',)

class FAModeAdmin(admin.ModelAdmin):
    list_display = ('Id','EquipmentNo','Line','StationLine','QuestionDesc'
                    ,'EssentialIssues','Solution','RepairTime','QuestionClassify'
                    ,'Analyst','AttachmentPath','Remark','CreateTime'
                    ,'UpdatedTime')
    search_fields = ('EquipmentNo',)
    ordering = ('Id',)
admin.site.register(ProjectsName,ProjectsNameAdmin)
admin.site.register(Customers,CustomersAdmin)
admin.site.register(BU,BUAdmin)
admin.site.register(EquipmentVendor,EquipmentVendorAdmin)
admin.site.register(EquipmentType,EquipmentTypeAdmin)
admin.site.register(Station,StationAdmin)
admin.site.register(QuestionClass,QuestionClassAdmin)
admin.site.register(EquipmentNumber,EquipmentNumberAdmin)
admin.site.register(FAMode,FAModeAdmin)
