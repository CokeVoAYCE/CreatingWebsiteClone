from datetime import datetime

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

from cammings.models import Camming


@csrf_exempt
@cache_page(900)
@gzip_page
@require_http_methods(["GET"])
def welcome(request):
    if request.method == 'GET':
        print(request.headers)
        print("----------\n", request)
        return render(request, "website/welcome.html",
                        {"cammings": Camming.objects.all()})
    elif request.method == 'POST':
        return HttpResponseNotFound("POST method is not allowed")

def date(request):
    if request.method == 'GET':
        print(request.headers)
        print("----------\n", request)
        return HttpResponse("The datetime is: " + str(datetime.now()))

def about(request):
    return HttpResponse("I'm Coke learning Django")