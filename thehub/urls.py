from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/api/achievements/<game>', views.get_achievements),
    path('/api/achievements/gain/<achiv>', views.gain_achievement),
    path('/api/me', views.get_profile),
    path('/api/gamesave/get/<game>', views.get_game_save),
    path('/api/gamesave/save/<game>',views.save_game_data),
    path('/developer/<dev>', views.dev_page),
    path('/devtools', views.developer_tools),
    path('/panel', views.dev_panel),
    path('/panel/delete/<game>', views.dev_panel_delete_game),
    path('/panel/update/<game>', views.dev_panel_update_game),
    path('/panel/askbecome', views.dev_panel_become_developer),
    path('/panel/achievements/<game>/add', views.dev_panel_add_achievement),
    path('/panel/achievements/<achiv>/delete', views.dev_panel_delete_achievement),
    path('/panel/add-game', views.dev_panel_add_game),
    path('/game/<game>', views.view_game),
    path('/game/<game>/download', views.download_game),
]