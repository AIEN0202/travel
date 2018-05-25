from django.shortcuts import render

# Create your views here.
def reviewindex(request):
    return render(request,'review/ReviewHome.html',locals())
