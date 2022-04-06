from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/panel', views.dev_panel),
    path('/panel/add-game', views.dev_panel_add_game),
    path('/game/<game>', views.view_game),
    path('/game/<game>/download', views.download_game),
]