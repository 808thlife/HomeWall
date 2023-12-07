from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    pass


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            if user.is_staff:
                login(request, user)
                return HttpResponseRedirect(reverse("core:index"))
            else:
                login(request,user)
                print("something")
                return HttpResponse("you are an ordinary user") 
                #IT SHOULD REDIRECT USER TO USERUI PAGE. WILL IMPLEMENT IT LATER
        else:
            return render(request, "accounts/pages-login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "accounts/pages-login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("accounts:login"))

