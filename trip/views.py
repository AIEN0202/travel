from django.shortcuts import render
# from django.core.files.storage import fileSystemStorage
# from . import modelscreate

def trip(request):
    context = "the trip page"
    return render(request,'trip/trip.html',locals())