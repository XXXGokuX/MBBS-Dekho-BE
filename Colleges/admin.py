from django.contrib import admin
from .models import College,CollegeInfo,CollegeMedia,University,FeeStructure
# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    prepopulated_fields= {'college_slug': ('college_name',)}

admin.site.register(College,CollegeAdmin)
admin.site.register(CollegeInfo)
admin.site.register(CollegeMedia)
admin.site.register(University)
admin.site.register(FeeStructure)