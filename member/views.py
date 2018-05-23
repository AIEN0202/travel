from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'member/index.html',locals())

def signup(request):
    return render(request,'member/signup.html',locals())
