from django.http import FileResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import AchievementSerializer, GameSaveSerializer, ProfileSerializer
from vgh.models import Profile

def index(request):
    caths = GameCathegory.objects.all()
    if "game" in request.GET:
        games = Game.objects.filter(title__icontains=request.GET["game"]).all()
    elif "cath" in request.GET:
        games = Game.objects.filter(cathergory=request.GET["cath"]).all()
    else:
        games = Game.objects.all()
    return render(request, "thehub/index.html", {"games": games, "cathegories": caths})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_achievements(request, game):
    achivs = Achievement.objects.filter(game=game).all()
    ser = AchievementSerializer(achivs, many=True)
    return JsonResponse(ser.data, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def gain_achievement(request, achiv):
    achivement = Achievement.objects.filter(id=achiv).first()
    gained = GainAchievement(achievement=achivement, user=request.user)
    gained.save()
    return JsonResponse({"data": "Trofeo guadagnato!"}, safe=False)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    ser = ProfileSerializer(profile)
    return JsonResponse(ser.data, safe=False)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_game_save(request, game):
    gameSave = GameSave.objects.filter(game=game).first()
    ser = GameSaveSerializer(gameSave)
    return JsonResponse(ser.data, safe=False)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def save_game_data(request, game):
    save = GameSave.objects.filter(user=request.user, game=game).first()
    if save:
        save.data = request.POST["data"]
        save.save()
        return JsonResponse({"data": "Dati salvati!"}, safe=False)
    else:
        game = Game.objects.filter(id=game).first()
        save = GameSave(data=request.POST["data"], user=request.user, game=game)
        return JsonResponse({"data": "Dati salvati!"}, safe=False)

def dev_panel_become_developer(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, "thehub/becomedev.html")
        else:
            devReq = DevRequest(text=request.POST["text"], user=request.user)
            devReq.save()
            return redirect("/thehub")
    else:
        return redirect("/login")

def dev_page(request, dev):
    dev = User.objects.filter(username=dev).first()
    profile = Profile.objects.filter(user=dev).first()
    games = Game.objects.filter(developer=dev).all()
    return render(request, "thehub/devpage.html", {"developer": dev, "prof": profile, "games": games})

def developer_tools(request):
    return render(request, "thehub/devtools.html")

def view_game(request, game):
    g = Game.objects.filter(id=game).first()
    return render(request, "thehub/viewgame.html", {"game": g})

def dev_panel_delete_game(request,game):
    g = Game.objects.filter(id=game).first()
    g.delete()
    return redirect("/thehub/panel")

def dev_panel_update_game(request, game):
    if request.user.is_authenticated:
        if request.method == 'GET':
            cats = GameCathegory.objects.all()
            g = Game.objects.filter(id=game).first()
            achivs = Achievement.objects.filter(game=g).all()
            return render(request, "thehub/updategame.html", {"game": g, "cathegories": cats, "achievements": achivs})
        else:
            g = Game.objects.filter(id=game).first()
            g.title = request.POST["title"]
            g.cover = request.FILES["cover"]
            g.description = request.POST["desc"]
            g.pegi = request.POST["pegi"]
            g.files = request.FILES["gamefiles"]
            g.cathergory = GameCathegory.objects.filter(title=request.POST["cathegory"]).first()
            g.save()
            return redirect("/thehub/panel")
    else:
        return redirect("/login")

def dev_panel_add_achievement(request, game):
    if request.user.is_authenticated:
        if request.method == 'GET':
            g = Game.objects.filter(id=game).first()
            return render(request, "thehub/addachievement.html", {"game": g})
        else:
            g = Game.objects.filter(id=game).first()
            achiv = Achievement(title=request.POST["title"], description=request.POST["desc"], difficulty=request.POST["difficulty"], game=g)
            achiv.save()
            return redirect(f"/thehub/panel/update/{game}")
    else:
        return redirect("/login")

def dev_panel_delete_achievement(request, achiv):
    ach = Achievement.objects.filter(id=achiv).first()
    g = ach.game
    ach.delete()
    return redirect(f"/thehub/panel/update/{g.id}")

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
    g.downloads += 1
    g.save()
    return FileResponse(open(g.files.path, "rb"), as_attachment=True)

def dev_panel(request):
    if request.user.is_authenticated:
        games = Game.objects.filter(developer=request.user).all()
        return render(request, "thehub/devpanel.html", {"games": games})
    else:
        return redirect("/login")