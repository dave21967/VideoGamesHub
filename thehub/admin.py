from django.contrib import admin
from .models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date','downloads']

class CathegoryAdmin(admin.ModelAdmin):
    list_display = ['title']

class AchievementAdmin(admin.ModelAdmin):
    list_display = ['id','title','game','difficulty']

admin.site.register(Game, GameAdmin)
admin.site.register(GameCathegory, CathegoryAdmin)
admin.site.register(Achievement, AchievementAdmin)