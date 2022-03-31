from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
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
            post = Post.objects.filter(id=post).first()
            com = Comment(user=request.user, post=post, text=request.POST["text"])
            com.save()
            return redirect(request.META["HTTP_REFERER"])
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

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")