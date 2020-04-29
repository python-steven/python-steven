from django.urls import path

from .views import *

app_name ="FA"

urlpatterns = [
	path("add-projects/",AddProject,name="Import_models"),
	path("modify-projects/",ModifyProject,name="Import_models"),
	path("del-projects/",DeleteProject,name="Import_models"),
]