from django.contrib import admin
from myApp.models import *

from .models import customUser

class customUser_Display(admin.ModelAdmin):
    list_display = ['username']

admin.site.register(customUser, customUser_Display)
admin.site.register(studentModel)
admin.site.register(SubjectModel)

admin.site.register(MarkModel)
