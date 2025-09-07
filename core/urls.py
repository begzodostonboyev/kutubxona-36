from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('1-topshiriq/',mualliflar_view),
    path('2-topshiriq/<int:muallif_id>/',tanlangan_muallif_view),
    path('3-topshiriq/',kitoblar_view ),
]
