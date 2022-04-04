from django.shortcuts import render, redirect
from .models import *

def index(request):
    if "game" in request.GET:
        games = Game.objects.filter(title__icontains=request.GET["game"]).all()
    else:
        games = Game.objects.all()
    return render(request, "thehub/index.html", {"games": games})

def dev_panel(request):
    if request.user.is_authenticated:
        games = Game.objects.filter(developer=request.user).all()
        return render(request, "thehub/devpanel.html", {"games": games})
    else:
        return redirect("/login")