from django.urls import path

from .views import *

app_name ="FA"

urlpatterns = [
	path("Get-Projects/",GetProject,name="GetProjects"),
	path("Add-Projects/",AddProject,name="AddProjects"),
	path("Modify-Projects/",ModifyProject,name="ModifyProject"),
	path("Delete-Projects/",DeleteProject,name="DeleteProject"),


	path("Get-Customers/",GetCustmoers,name="GetCustmoers"),
	path("Add-Customers/",AddCustomer,name="AddCustomer"),
	path("Modify-Customers/",ModifyCustomer,name="ModifyCustomer"),
	path("Delete-Customers/",DeleteCustomer,name="DeleteCustomer"),


	path("Get-BU/",GetBUs,name="GetBUs"),
	path("Add-BU/",AddBUs,name="AddBUs"),
	path("Modify-BU/",ModifyBU,name="ModifyBU"),
	path("Delete-BU/",DeleteBU,name="DeleteBU"),


	path("Get-Vendor/",GetVendors,name="GetVendors"),
	path("Add-Vendor/",AddVendor,name="AddBUs"),
	path("Modify-Vendor/",ModifyVendor,name="ModifyVendor"),
	path("Delete-Vendor/",DeleteVendor,name="DeleteVendor"),


	path("Get-Type/",GetTypes,name="GetTypes"),
	path("Add-Type/",AddType,name="AddType"),
	path("Modify-Type/",ModifyType,name="ModifyType"),
	path("Delete-Type/",DeleteType,name="DeleteType"),


	path("Get-Stations/",GetStations,name="GetStations"),
	path("Add-Station/",AddStation,name="AddStation"),
	path("Modify-Station/",ModifyStation,name="ModifyStation"),
	path("Delete-Station/",DeleteStation,name="DeleteStation"),


	path("Get-Questions/",GetQuestions,name="GetQuestions"),
	path("Add-Question/",AddQuestion,name="AddQuestion"),
	path("Modify-Question/",ModifyQuestion,name="ModifyQuestion"),
	path("Delete-Question/",DeleteQuestion,name="DeleteQuestion"),


	path("GET-Info/",GETInfo,name="GETInfo"),
	path("Add-EquipmentManage/",AddEquipmentManager,name="AddEquipmentManager"),
	path("Get-EquipmentManager/",GetEquipmentManager,name="GetEquipmentManager"),
	path("Modify-EquipmentManage/",ModifyEquipmentManager,name="ModifyEquipmentManager"),
	path("Delete-EquipmentManage/",DeleteEquipmentManager,name="DeleteEquipmentManager"),

	path("GET-FT-info/",GETFTINFO,name="GETFTINFO"),
	path("Add-FT/",AddFT,name="AddFT"),
	path("Get-FA-Modes/",GETFAModes,name="GETFAModes"),
	path("Delete-FT/",DeleteFT,name="DeleteFT"),
	path("Modify-FT/",ModifyFT,name="ModifyFT"),
	path("GET-FT-query-info/",GETQueryInfo,name="GETQueryInfo"),


]


