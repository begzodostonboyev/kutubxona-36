from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group
import site

class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id','ism', 'guruh', 'kurs', 'kitobi_soni')
    list_display_links = ('id', 'ism') #link

class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'ish_boshlash', 'ish_tugashi')
    list_filter = ('ish_boshlash',)
    search_fields = ('ism',)
    search_help_text = "ismi bo'yicha qidiring."


class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'tugulgan_sana', 'kitob_soni', 'tirik')
    list_display_links = ('id', 'ism')
    search_fields = ('ism',)
    search_help_text = "ism bo'yicha qidiring"
    list_filter = ('tirik',)
    list_editable = ('kitob_soni', 'tirik')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('talabalar', 'kitoblar', 'adminlar', 'olingan_sana', 'berilgan_sana')
    date_hierarchy = 'olingan_sana'


admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kitob)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Record, RecordAdmin)

admin.site.site_header = "Kutubxona paneli"
admin.site.site_title = "Kutubxona boshqaruvi"
admin.site.index_title = "KUTUBXONA"

admin.site.unregister(Group)
admin.site.unregister(User)

