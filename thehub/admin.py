from django.contrib import admin
from .models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date','downloads']

class CathegoryAdmin(admin.ModelAdmin):
    list_display = ['title']

class AchievementAdmin(admin.ModelAdmin):
    list_display = ['id','title','game','difficulty']

class DevRequestAdmin(admin.ModelAdmin):
    list_display = ['id','approved']

class GainAchievementAdmin(admin.ModelAdmin):
    list_display = ['id','achievement','user']

class GameSaveAdmin(admin.ModelAdmin):
    list_display = ['id','game','user']

admin.site.register(Game, GameAdmin)
admin.site.register(GameCathegory, CathegoryAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(DevRequest, DevRequestAdmin)
admin.site.register(GainAchievement, GainAchievementAdmin)
admin.site.register(GameSave, GameSaveAdmin)