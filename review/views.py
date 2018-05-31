from django.shortcuts import render,redirect
from django.db import connection
# Create your views here.
def reviewindex(request):
    if request.method=="POST":
        TextArea = request.POST['TextArea']
        sql = "insert into cccc.Review (idReview, Reviewcol,Star) values(%s, %s, %s)"
        with connection.cursor() as cursor:
            cursor.execute(sql,('1',TextArea,'1'))

    return render(request,'review/ReviewHome.html',locals())

def create(request):
    return render(request,'review/create.html',locals())
