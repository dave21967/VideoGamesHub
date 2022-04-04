from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('feed', views.feed),
    path('feed/comment/<post>', views.add_comment),
    path('feed/view/<slug>', views.single_post),
    path('login', views.auth),
    path('logout', views.log_out),
    path('me', views.profile),
    path('signup', views.signup),
]