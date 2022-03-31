from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','views','pub_date','author']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','profile_pic']


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)