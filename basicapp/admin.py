from django.contrib import admin
from basicapp.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):

    fields = ['email','first_name','last_name']

    search_fields = ['email','first_name','last_name']

    list_filter = ['email','first_name','last_name']

    list_display = ['email','first_name','last_name']

admin.site.register(User,UserAdmin)

