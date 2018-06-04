from django.shortcuts import render
# from django.core.files.storage import fileSystemStorage
# from . import modelscreate
# We need this in order to return Json format
from django.http import JsonResponse,HttpResponse
from member import models as m1
from .models import Restaurant as rest


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
    #Define a variable for ajax to into.
    CurrentFilter = request.GET.get('CurrentFilter',None).strip()

    #Create Empty list for input
    ImList = []

    #Get Everything from database
    RestInfo = rest.objects.filter(type='American (Traditional)')

    #Loop through the Query Objects

    for x in RestInfo:
        #Create a new Dictionary
        ImDict = {}
        RestName = x.title
        print(RestName)
        ImDict['RestName'] = RestName
        RestImg = x.imgsrc
        ImDict['RestImg'] = RestImg
        RestId = x.resid
        ImDict['Resid'] = RestId

        #Pass in the data to list
        ImList.append(ImDict)

    return JsonResponse(ImList,safe=False)
