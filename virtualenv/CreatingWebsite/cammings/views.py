from django.views import View
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.urls import path
from django.views.decorators.cache import cache_control, cache_page
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound


# def error_handler(request, exception=None):
#     return HttpResponseNotFound("<h1>Page Not Found</h1>", status=404)
#
#
# def page_not_found(request):
#     raise ViewDoesNotExist
#
# urlpatterns = [
#     path('404/', page_not_found),
# ]
#
# handler403 = error_handler
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from django.forms import modelform_factory

from django.shortcuts import render, get_object_or_404, redirect

from .models import Camming   #import cammings class from models
from .models import Room   #import rooms class from models



def detail(request, id):
    camming = get_object_or_404(Camming, pk=id)
    return render(request, "cammings/detail.html", 
                  {"camming": camming})

def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, "cammings/rooms_list.html",
            {"rooms": rooms}) 
    
CammingForm = modelform_factory(Camming, exclude=[])
    
def new(request):
    if request.method == "POST":
        form = CammingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = CammingForm()
    return render(request, "cammings/new.html", {"form": form})

