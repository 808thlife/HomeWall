from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def rulesView(request):
    return render(request, "core/rules.html")

def users(request):
    return render(request, "core/users.html")