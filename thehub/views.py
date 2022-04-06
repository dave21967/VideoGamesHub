from django.http import FileResponse
from django.shortcuts import render, redirect
from .models import *

def index(request):
    if "game" in request.GET:
        games = Game.objects.filter(title__icontains=request.GET["game"]).all()
    else:
        games = Game.objects.all()
    return render(request, "thehub/index.html", {"games": games})

def view_game(request, game):
    g = Game.objects.filter(id=game).first()
    return render(request, "thehub/viewgame.html", {"game": g})

def dev_panel_add_game(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            cats = GameCathegory.objects.all()
            return render(request, "thehub/addgame.html", {"categories": cats})
        else:
            cath = GameCathegory.objects.filter(title=request.POST["cathegory"]).first()
            g = Game(title=request.POST["title"], cover=request.FILES["cover"], description=request.POST["desc"], files=request.FILES["gamefiles"], pegi=request.POST["pegi"], cathergory=cath, developer=request.user)
            g.save()
            return redirect("/thehub/panel")
    else:
        return redirect("/login")

def download_game(request, game):
    g = Game.objects.filter(id=game).first()
    return FileResponse(open(g.files.path, "rb"), as_attachment=True)

def dev_panel(request):
    if request.user.is_authenticated:
        games = Game.objects.filter(developer=request.user).all()
        return render(request, "thehub/devpanel.html", {"games": games})
    else:
        return redirect("/login")