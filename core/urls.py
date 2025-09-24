from django.contrib import admin
from django.contrib.auth.urls import urlpatterns
from django.urls import path
from main.views import *

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', home_view),
    path('talabalar/',talabalar_view),
    path('talabalar/<int:pk>/update/', talaba_update_view),
    path('talaba/<int:pk>/', student_deteils_view),
    path('talabalar/<int:pk>/delete/', talaba_delete_view),
    path('mualliflar/', mualliflar_view),
    path('muallif_details/<int:muallif_id>/', tanlangan_muallif_view),
    path('muallif_details/<int:muallif_id>/delete/', muallif_delete_view),
    path('kitoblar/', kitoblar_view),
    path('kitoblar_deteils/<int:kitob_id>/',kitob_deteils_view),
    path('kitoblar/<int:kitob_id>/delete/confirm/',kitob_delete_confirm_view),
    path('kitoblar/<int:kitob_id>/delete/',kitob_delete_view),
]