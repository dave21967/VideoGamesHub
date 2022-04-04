from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from vgh.models import Post, Comment

def index(request):
    return render(request, "index.html")

def feed(request):
    if not request.GET:
        posts = Post.objects.order_by("pub_date").all()
    else:
        posts = Post.objects.filter(tags__icontains=request.GET["tag"]).all()
    return render(request, "feed.html", {"posts": posts})

def single_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(post=post).all()
    if post:
        return render(request, "post.html", {"post": post, "comments": comments})
    else:
        return HttpResponse("Nessun post trovato!")

def add_comment(request, post):
    if request.user.is_authenticated:
        if request.POST:
            pst = Post.objects.filter(id=post).first()
            com = Comment(user=request.user, post=pst, text=request.POST["text"])
            com.save()
            return redirect(f"/feed/view/{pst.slug}")
    else:
        return HttpResponse(request, "Error: user not authenticated")


def auth(request):
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        user = authenticate(username=request.POST["username"],password=request.POST["password"])
        if user is not None:
            print("user found")
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("No user found", status=401)

def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    else:
        user = User(username=request.POST["username"], email=request.POST["email"])
        user.set_password(request.POST["password"])
        group = Group.objects.filter(name="comune").first()
        user.save()
        user.groups.add(group)
        return redirect("/login")

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")

def profile(request):
    if request.user.is_authenticated:
        user = User.objects.filter(username=request.user).first()
        is_dev = False
        if user.groups.filter(name="developer") or user.is_superuser:
            is_dev = True
        return render(request, "profile.html", {"user": user, "isDev": is_dev})
    else:
        return redirect("/login")