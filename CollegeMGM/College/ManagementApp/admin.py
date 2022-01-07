from django.contrib import admin
from . models import Dept,Prof,Student

class DeptAdmin(admin.ModelAdmin):
    list_display = ['did','dep_name']
admin.site.register(Dept,DeptAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['sid','name','rollno']
admin.site.register(Student,StudentAdmin)

class ProAdmin(admin.ModelAdmin):
    list_display = ['prof_name','sub']
admin.site.register(Prof,ProAdmin)
