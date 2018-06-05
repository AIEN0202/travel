from django.shortcuts import render
# from django.core.files.storage import fileSystemStorage
# from . import modelscreate
# We need this in order to return Json format
from django.http import JsonResponse,HttpResponse
from member import models as m1
from .models import Restaurant as rest
from .models import Hotel as hotel
from .models import Attraction as attr

# def trip(request):
    # 	if request.method == 'POST':
	# 	""=request.POST.get('')
	# return render(request,'trip/trip.html',locals())


def trip(request):
    context = "the trip page"
    if 'user' in request.session:
        useris = request.session['user']
        print("GET {}".format(useris))
        isLogin = True
    else:
        print("NO GET")
    if request.method == "POST":
        tripname = request.POST["tripname"]
        miantrip_country = request.POST["miantrip_country"]
        miantrip_region = request.POST["miantrip_region"]
        departyear = request.POST["departyear"]
        departmonth = request.POST["departmonth"]
        departday = request.POST["departday"]
        tripday = request.POST["tripday"]
        Travelers = request.POST["Travelers"]
        Travelpath = request.POST["Travelpath"]
        check = request.POST.getlist("Style")
        Stylelist = '/'.join(check)
        print(tripname)
        print('')
        print(miantrip_country)
        print('')
        print(miantrip_region)
        print('')
        print(departyear+"/"+departmonth+"/"+departday)
        print('')
        print(tripday)
        print('')
        print(Travelers)
        print('')
        print(Travelpath)
        print('')
        print(Stylelist)
        print('')
        
    return render(request,'trip/trip.html',locals())

#Create a function for Ajax to call later
def Wchange(request):
    print("HI")
    #Define a variable for ajax to into.
    CurrentFilter = request.GET.get('CurrentFilter',None).strip()
    CheckForSelect = request.GET.get('CheckForSelect',None).strip()
    #Create Empty list for input
    ImList = []
    #Get Everything from database
    if CheckForSelect == "Attraction":
        Info = attr.objects.filter(type=CurrentFilter)
    elif CheckForSelect == "Restuarant":
        Info = rest.objects.filter(type=CurrentFilter)
    elif CheckForSelect == "Hotel":
        Info = hotel.objects.filter(type=CurrentFilter)
    else:
        print("Faile")
    #Loop through the Query Objects

    for x in Info:
        #Create a new Dictionary
        ImDict = {}
        Name = x.title
        ImDict['Name'] = Name
        Img = x.imgsrc
        ImDict['Img'] = Img
        if CheckForSelect == "Attraction":
            Idlala = x.idattraction
        elif CheckForSelect == "Restuarant":
            Idlala = x.resid
        elif CheckForSelect == "Hotel":
            Idlala = x.id_hotel
        
        ImDict['Id'] = Idlala

        #Pass in the data to list
        ImList.append(ImDict)

    return JsonResponse(ImList,safe=False)
