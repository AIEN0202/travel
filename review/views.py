from django.shortcuts import render,redirect
from django.db import connection
from .models import Review as rw
from member import models as m1
from django.db.models import Avg,Count
import random
# Create your views here.
def reviewindex(request):
    TupleOfReview = []
    isFooterShow=False
    if 'user' in request.session:
        useris = request.session['user']
        isLogin = True
    else:
        return redirect('../member/')

    # This is for filter out the place name, and get the range for stars
    MainPlace = rw.objects.filter(typeplace="Happy")
    HI3 = MainPlace.aggregate(Avg('rating'))
    # print(HI3)
    TOTALREVIEWC = MainPlace.aggregate(Count('contentofreview'))
    if HI3['rating__avg'] is not None:
        AVGGSTARR = range(round(HI3['rating__avg']))
        AVGBSTARR = range(5-round(HI3['rating__avg']))
    else:
        AVGGSTARR = range(0)
        AVGBSTARR = range(0,5)
    ShowAllHasTag = MainPlace.values('hastable')
    # print(ShowAllHasTag)
    HasTList = []
    for showHastab in ShowAllHasTag:
        if showHastab!=None:
            HasTList = HasTList + showHastab['hastable'].split(',')
    print(HasTList)

    # Get review object within the database
    members = rw.objects.filter(typeplace="Happy").order_by('datereview')

    # Using for loop to seperate the items we need.
    for memberreview in members:

        # memberreview.memberid will return Member object
        AllName = memberreview.memberid.membername.split('/')
        RealName = AllName[0] + " " + AllName[1]
        RealContent = memberreview.contentofreview.split('\r\n')
        RealGStar = range(int(memberreview.rating))
        RealBStar = range(5-int(memberreview.rating))
        # print(RealBStar)
        TupleOfReview.append((RealContent,RealGStar,RealName,memberreview.datereview,RealBStar))

    if request.method=="POST":
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
        return redirect('/review')

    return render(request,'review/ReviewHome.html',locals())

def create(request):
    return render(request,'review/create.html',locals())
