from django.urls import path

from .views import *

app_name ="analysis"

urlpatterns = [
    path(r'information/',Information_Box,name="Information_Box"),
    path(r'',information_app,name="Information_app"),
]