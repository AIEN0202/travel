from django.shortcuts import render
# from django.core.files.storage import fileSystemStorage
# from . import modelscreate
# We need this in order to return Json format
from django.http import JsonResponse,HttpResponse
from member import models as m1
from .models import Restaurant as rest
from member import member_models as MB
import random
from .models import Hotel as hotel
from .models import Attraction as attr

# def trip(request):
    # 	if request.method == 'POST':
	# 	""=request.POST.get('')
	# return render(request,'trip/trip.html',locals())


def trip(request):
    context = "the trip page"
    tripid_fromsession = None
    triptotalday = None
    triptotalpanel = None

    if 'user' in request.session:
        useris = request.session['user']
        print("GET {}".format(useris))
        isLogin = True

        if_trip_exist = MB.Member()
        trip_day_res = if_trip_exist.select_one('SELECT count(B.idday) FROM travel.itinerary as A, travel.itinerary_day as B where A.TripID = B.TripID and A.idMember = %s;', useris)
        trip_res = if_trip_exist.select_one('SELECT count(TripID) FROM travel.itinerary where idMember = %s;', useris)

        if trip_res is not None :
            if trip_res[0] != 0 and trip_day_res[0] == 0:
                print('start dalete')
                if_trip_exist.excute_sql('delete from travel.itinerary where idMember = %s;', useris)
            else:
                # print('pass' + trip_res[0] + "/" + trip_day_res[0])
                pass
        else:
            pass

    else:
        print("NO GET")

    if 'tripid' in request.session:
         tripid_fromsession = request.session['tripid']
    else:
        pass
    
    if 'tpday' in request.session:
         triptotalday = range(2, int(request.session['tpday'])+1) 
         triptotalpanel = range(1, int(request.session['tpday'])+1) 
    else:
        pass

    if request.method == "POST":  
        tripid = random.randint(700000, 799999)   
        userid = request.session['user']   
        tripname = request.POST["tripname"]
        miantrip_country = request.POST["miantrip_country"]
        miantrip_region = request.POST["miantrip_region"]
        departyear = request.POST["departyear"]
        departmonth = request.POST["departmonth"]
        departday = request.POST["departday"]
        totaltripdate = departyear+"/"+departmonth+"/"+departday
        tripday = request.POST["tripday"]
        Travelers = request.POST["Travelers"]
        Travelpath = request.POST["Travelpath"]
        check = request.POST.getlist("Style")
        Stylelist = '/'.join(check)
        trip_data = MB.Member()
        trip_data.excute_sql("INSERT INTO travel.itinerary (TripID, idMember, TripName, Day, Arrival, Travelers, Paced, Style, idCountry, idRegion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", tripid, userid, tripname, tripday, totaltripdate, Travelers, Travelpath, Stylelist, miantrip_country, miantrip_region)

        request.session['tripid'] = tripid
        request.session.modified = True

        request.session['tpday'] = tripday
        request.session.modified = True

        tripid_fromsession = request.session['tripid']
        triptotalday = range(2, int(request.session['tpday'])+1) 
        triptotalpanel = range(1, int(request.session['tpday'])+1) 

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


def trippost(request):
    # request.session.clear()
    # isFooterShow = True
    # print("XDDDD")
    if request.method == "POST":
        if 'tpday' in request.session:
            totalday = int(request.session['tpday'])+1
            for days in range(1,totalday):
                print('day{}'.format(days))
                attrname = 'i_daysp'+str(days)
                hotelname = 'i_daysh'+str(days)
                resname = 'i_daysr'+str(days)
                get_attr= request.POST[attrname][:-2] 
                get_hot= request.POST[hotelname][:-2]
                get_res= request.POST[resname][:-2]
                tripid = request.session['tripid']
                print(tripid)
                print(get_attr) 
                print(get_hot) 
                print(get_res) 
                print('')
                trip_data = MB.Member()
                trip_data.excute_sql("insert into itinerary_day values(%s, %s, %s, %s, %s);", days, get_hot, get_res, tripid, get_attr)

        else:
            pass

    


         

    return render(request, 'trip/trip.html', locals())


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
    elif CheckForSelect == "Restaurant":
        Info = rest.objects.filter(type=CurrentFilter)
    elif CheckForSelect == "Hotel":
        Info = hotel.objects.filter(type=CurrentFilter)
    else:
        if CheckForSelect == "Attraction":
            Info = attr.objects.all()
        elif CheckForSelect == "Restaurant":
            Info = rest.objects.all()
        elif CheckForSelect == "Hotel":
            Info = hotel.objects.all()
        
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
        elif CheckForSelect == "Restaurant":
            Idlala = x.resid
        elif CheckForSelect == "Hotel":
            Idlala = x.id_hotel
        
        ImDict['Id'] = Idlala
        print(ImDict['Id'])
        
        #Pass in the data to list
        ImList.append(ImDict)

    return JsonResponse(ImList,safe=False)
