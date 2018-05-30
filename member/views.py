from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'member/index.html',locals())

def signup(request):
    if request.method == "POST":
        lastname = request.POST["member_lastname"]
        firstname = request.POST["member_firstname"]
        email = request.POST["member_email"]
        birthday = request.POST["member_birthday"]
        country = request.POST["member_country"]
        region = request.POST["member_region"]
        gender = request.POST["member_gender"]
        check = request.POST.getlist("member_check")
        print(lastname + "/" +firstname+ "/" +email+ "/" +birthday+ "/" +country+ "/" +region+ "/" +gender)
        print(check)
    return render(request,'member/signup.html',locals())

def login(request):
    email = request.POST["loginmail"]
    pwd = request.POST["loginpwd"]
    print(email)
    return render(request,'member/index.html',locals())
