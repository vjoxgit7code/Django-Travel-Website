from django.http import HttpResponse
from django.shortcuts import render
from .  models import place
from . models import person
#Create your views here.

def dj(request):
    obj=place.objects.all()
    per=person.objects.all()
    return render(request,"index.html",{'result':obj,'result1':per})




