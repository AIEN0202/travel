from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
# Create your views here.
def res(request):
    # title = "res detail" 
    return render(request,'res/res.html',locals())

def booking(request):
    # title = "res detail" 
    return render(request,'res/booking.html',locals())

def box(request):
# title = "res detail" 
    return render(request,'res/lightbox.html',locals())


