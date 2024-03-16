from django.contrib import admin
from .models import Tblemployeeprofile1, Lkptblgender

class Tblemployeeprofile1Admin(admin.ModelAdmin):
    def get_list_display(self, request):
        # Get all field names from the model
        return [field.name for field in Tblemployeeprofile1._meta.get_fields()]

# Register your models here.
admin.site.register(Tblemployeeprofile1, Tblemployeeprofile1Admin)



class LkptblgenderAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        # Get all field names from the model
        return [field.name for field in Lkptblgender._meta.get_fields()]

# Register your models here.
admin.site.register(Lkptblgender, LkptblgenderAdmin)