from django.shortcuts import render
import datetime
from django.utils import timezone
from django.contrib.sessions.models import Session
# Create your views here.
from .models import Clent
from .forms import ClentForm
from django.utils import cache
from dg.urls import *

def index(request):
    now_time = str(datetime.datetime.now())
    now_time_index = datetime.datetime.now()
    s = Session.objects.all()
    form =ClentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'index.html', locals())
def sitemap(request):
    return render(request, 'sitemap.xml', locals())
def robots(request):
    return render(request, 'robots.txt', locals())
def ads(request):
    return render(request, 'ads.txt', locals())
