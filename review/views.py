from django.shortcuts import render,redirect
from django.db import connection
from .models import Review as rw
from member import models as m1
import random
# Create your views here.
def reviewindex(request):
    TupleOfReview = []
    # Get review object within the database
    members = rw.objects.all()
    # Using for loop to seperate the items we need.
    for memberreview in members:
        # memberreview.memberid will return Member object
        TupleOfReview.append((memberreview.contentofreview,memberreview.rating,memberreview.memberid.idmember))
    if request.method=="POST":
        TextArea = request.POST['TextArea']
        # Get random ID
        ReviewID = random.randint(200000, 299999)
        PlaceID = '1'
        mmm1 = 181445
        MemberID = m1.Member.objects.get(idmember=mmm1)
        StarCounts = request.POST['HStarCount']
        rw.objects.create(contentofreview = TextArea,memberid = MemberID,datereview = '2008/01/01',idreview = ReviewID,placeid = PlaceID,typeplace = 'Happy',rating = StarCounts)
        return redirect('/review')

    return render(request,'review/ReviewHome.html',locals())

def create(request):
    return render(request,'review/create.html',locals())
