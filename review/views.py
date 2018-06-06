from django.shortcuts import render,redirect
from django.db import connection
from .models import Review as rw
from .models import Attraction as at
from .models import Hotel as ht
from .models import Restaurant as rest
from member import models as m1
from django.db.models import Avg,Count
import random
# Create your views here.
def reviewindex(request):
    TupleOfReview = []

    #Check for login
    isFooterShow=False
    if 'user' in request.session:
        useris = request.session['user']
        isLogin = True
    else:
        return redirect('../member/')

    #Save data to session
    if request.method=="GET":
        pid = request.GET['placeide']
        request.session['placeide'] = pid
        request.session.modified = True

    #Judge Where to read database
    if pid.startswith('3'):
        CorrectPlace = at.objects.filter(idattraction = pid).get()
        print(CorrectPlace)
    elif pid.startswith('5'):
        CorrectPlace = rest.objects.filter(resid = pid).get()
    elif pid.startswith('6'):
        CorrectPlace = ht.objects.filter(id_hotel = pid).get()
    else:
        print("False")

    # Get the MainPlace by filter & order review by time
    MainPlace = rw.objects.filter(placeid = pid)
    reviews = rw.objects.filter(placeid = pid).order_by('-datereview')

    # This is for filter out the place name, and get the range for stars
    HI3 = MainPlace.aggregate(Avg('rating'))
    TOTALREVIEWC = MainPlace.aggregate(Count('contentofreview'))
    if HI3['rating__avg'] is not None:
        AVGGSTARR = range(round(HI3['rating__avg']))
        AVGBSTARR = range(5-round(HI3['rating__avg']))
    else:
        AVGGSTARR = range(0)
        AVGBSTARR = range(0,5)
    ShowAllHasTag = MainPlace.values('hastable')

    #Calculate Stars to show on the popover box
    StarsProgress = StarsProgressBar(MainPlace,TOTALREVIEWC)

    #Show Hastable
    HasTList = []
    for showHastab in ShowAllHasTag:
        if showHastab['hastable']!=None:
            if showHastab['hastable'] not in HasTList:
                HasTList = HasTList + showHastab['hastable'].split(',')
            else:
                pass
        else:
            pass
    HasTList = HasTList[1:]
    HasTList=set(HasTList)

    # Present Data onto detail box
    CorrectPlaceName = CorrectPlace.title
    CorrectPlaceType = CorrectPlace.type
    CorrectPlacePic = CorrectPlace.imgsrc
    if CorrectPlace.tel is None:
        CorrectPlacePhone = "none"
    else:
        CorrectPlacePhone = CorrectPlace.tel
    CorrectPlaceAddr = CorrectPlace.addr
    CorrectPlaceTime = CorrectPlace.time
    if CorrectPlace.time is '':
        CorrectPlaceTime = "Open 24 hours"
    else:
        CorrectPlaceTime = CorrectPlace.time

    # Using for loop to seperate the items we need.
    for memberreview in reviews:

        # memberreview.memberid will return Member object
        AllName = memberreview.memberid.membername.split('/')
        RealName = AllName[0] + " " + AllName[1]
        RealContent = memberreview.contentofreview.split('\r\n')
        RealGStar = range(int(memberreview.rating))
        RealBStar = range(5-int(memberreview.rating))
        # print(RealBStar)
        TupleOfReview.append((RealContent,RealGStar,RealName,memberreview.datereview,RealBStar))

    #Post

    if request.method=="POST":
        print('in post')
        TextArea = request.POST['TextArea']
        SeperateTextArea = TextArea.split("#")
        TrueTextArea = SeperateTextArea[0]
        HastagText = ",".join(SeperateTextArea[1:])
        # Get random ID
        ReviewID = random.randint(200000, 299999)
        DateOfReview = request.POST['HReviewTime']
        PlaceID = '1'
        MemberID = m1.Member.objects.get(idmember=useris[0])
        StarCounts = request.POST['HStarCount']
        rw.objects.create(contentofreview = TrueTextArea,memberid = MemberID,datereview = DateOfReview,idreview = ReviewID,placeid = PlaceID,typeplace = 'Happy',rating = StarCounts,hastable = HastagText)
        print('post func')

        if 'placeide' in request.session:
            placeide = request.session['placeide']
            return redirect('/review/?placeide={}'.format(placeide))
        else:
            return redirect('/trip')

    print('after post func')
    return render(request,'review/ReviewHome.html',locals())

def StarsProgressBar(M,T):
    #This is a Table of stars
    StarTable = {}
    #Get the total Count of review
    ThisisProgressBar = T['contentofreview__count']
    # FStar = M.filter(rating=5).aggregate(Count('rating'))
    if ThisisProgressBar != 0:
        for x in range(1,6):
            FStar = M.filter(rating=x).aggregate(Count('rating'))
            StarTable[str(x)+'Star'] = str(round((FStar['rating__count']/ThisisProgressBar)*100))+"%"
    else:
        for x in range(1,6):
            StarTable[str(x)+'Star'] = str(0)+"%"
    return StarTable
