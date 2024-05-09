from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Filter

def add_filter(request):
    if request.method == "POST":
        domain = request.POST["domain"]
        action = request.POST["action"]
        category = request.POST["category"]

        f = Filter(category = category, action = action, domain = domain)
        f.save()

        return HttpResponseRedirect(reverse("core:filter_view"))

def edit_filter(request, ID):
    if request.method == "POST":
        filter = Filter.objects.get(id = ID)

        domain = request.POST["domain"]
        action = request.POST["action"]
        category = request.POST["category"]

        filter.domain = domain
        filter.action = action
        filter.category = category
        filter.save()

        return HttpResponseRedirect(reverse("core:filter_view"))

def delete_filter(request, ID):
    if request.method == "POST":
        filter = Filter.objects.get(id = ID)
        filter.delete()
        return HttpResponseRedirect(reverse("core:filter_view"))

    return HttpResponse("INCORRECT METHOD!")
