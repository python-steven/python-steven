from django.urls import path

from .views import ModelstageID,SNinfo,Import_models,Import_SN,Box_Id,Alternative_query\
	,Modify_alterParCode,Delete_alterParCode,unbinding_query,Info_all_query,release_PartCode,remove_PartCode\
	,modify_PartCode,ReleaseAllPartCode,Add_Box,Download_binding_infos

app_name ="BoxID"

urlpatterns = [
	path("import-models/",Import_models,name="Import_models"),       			#信息导入界面的导入model
	path("import-SN/",Import_SN,name="Import_SN"),                   			#信息导入界面的SN
	# path("Get-Box/",Get_Box,name="Get_Box"),                         			#信息导入的界面的获取box
	path("Add-Box/",Add_Box,name="Add_Box"),                         			#信息导入的增加box

	path("Model-stage-ID/",ModelstageID,name="ModelstageID"),       			#输入的modelstageID查询的数据 绑定业务
	path("SN-info/",SNinfo,name="SNinfo"),                          			#输入的SN查询的数据           绑定业务
	path("Box-Id-check/",Box_Id,name="Box_Id"),                    				#输入的BoxId查询的数据        绑定业务

	path("unbinding-query/",unbinding_query,name="unbinding_query"),            # 解绑页面的查询
	path("release-partCode/",release_PartCode,name="release_PartCode"),         # 解绑
	path("remove-partCode/",remove_PartCode,name="remove_PartCode"),            # 删除
	path("modify-partCode/",modify_PartCode,name="modify_PartCode"),            # 修改数量
	path("Release-all-partCode/",ReleaseAllPartCode,name="ReleaseAllPartCode"), # 批量解绑

	path("alternative-query/",Alternative_query,name="Alternative_query"),
	path("modify-alterParCode/",Modify_alterParCode,name="Modify_alterParCode"),
	path("delete-alterParCode/",Delete_alterParCode,name="Delete_alterParCode"),



	path("info-all-query/",Info_all_query,name="Info_all_query"),
	path("download-binding-infos/",Download_binding_infos,name="Download_binding_infos"),
]