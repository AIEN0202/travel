from django.shortcuts import render,redirect
from . import member_models as Mbr
import random
from django.http import HttpResponse
import json

# Create your views here.


def index(request):
    request.session.clear()
    isFooterShow = True
    return render(request, 'member/index.html', locals())


def signup(request):
    if request.method == "POST":
        memberid = random.randint(100000, 199999)
        lastname = request.POST["member_lastname"]
        firstname = request.POST["member_firstname"]
        email = request.POST["member_email"]
        pwd = request.POST["member_pwd"]
        birthday = request.POST["member_birthday"]
        # country = request.POST["member_country"]
        country = 9001
        region = request.POST["member_region"]
        gender = request.POST["member_gender"]
        check = request.POST.getlist("member_check")
        checkstr = '/'.join(check)
        sign_data = Mbr.Member()
        sign_data.excute_sql("insert into travel.member (idMember, Membername, MemberEmail, MemberPassword, MemberBday, MemberGender, MemberidCountry, MemberHobby) values(%s, %s, %s, %s, %s, %s, %s, %s)",
                             memberid, (lastname + "/" + firstname), email, pwd, birthday, gender, country, checkstr)
        # print(lastname + "/" +firstname+ "/" +email+ "/" +birthday+ "/" +country+ "/" +region+ "/" +gender)
        # print(check)
        # print(type(check))
        # print(checkstr)

    get_city_data = Mbr.Member()
    citylist = get_city_data.select_all("SELECT * FROM travel.country")
    print(citylist)
    isFooterShow = True

    return render(request, 'member/signup.html', locals())


def login(request):
    isLogin = False
    if request.method == "POST":
        email = request.POST["loginmail"]
        pwd = request.POST["loginpwd"]
        # print(email)
        login_chexk = Mbr.Member()
        res = login_chexk.select_one(
            "select idMember from travel.member where MemberEmail = %s and MemberPassword = %s", email, pwd)
        # print(res[0])
        if res is not None and res[0] is not None:
            
            request.session['user'] = res
            request.session.modified = True

            return redirect('../member/Main_index')
        else:
            response = HttpResponse("<script>alert('login fail');location.href='/';</script>")
            return response
        

    return render(request, 'member/Main_index.html', locals())


def Main_index(request):
    isFooterShow = False

    get_city_data = Mbr.Member()
    citylist = get_city_data.select_all("SELECT * FROM travel.country")

    if 'user' in request.session:
        useris = request.session['user']
        print("GET {}".format(useris))
        isLogin = True
    else:
        print("NO GET")

    return render(request, 'member/Main_index.html', locals())

def trv_detail(request):
    isFooterShow = False

    if 'user' in request.session:
        useris = request.session['user']
        print("GET {}".format(useris))
        isLogin = True
    else:
        print("NO GET")

    return render(request, 'member/trv_detail.html', locals())


def mReg(request):
    if request.method == "GET":
        c_id = request.GET["country"]
        if c_id is not None:
            print("YES")
            get_region_data = Mbr.Member()
            Regionlist = get_region_data.select_all("SELECT * FROM travel.member_region where idCountry = %s",c_id)
            print(json.dumps(Regionlist))
            response = json.dumps({"Reglist" : Regionlist})
            return HttpResponse(response, content_type='application/json')

    return HttpResponse("HI")

def mainReg(request):
    if request.method == "GET":
        c_id = request.GET["country"]
        if c_id is not None:
            print("YES")
            get_region_data = Mbr.Member()
            Regionlist = get_region_data.select_all("SELECT * FROM travel.region where idCountry = %s",c_id)
            print(json.dumps(Regionlist))
            response = json.dumps({"Reglist" : Regionlist})
            return HttpResponse(response, content_type='application/json')

    return HttpResponse("HI")

def getStyle(request):
    if request.method == "GET":
        c_style = request.GET["style"]
        if c_style is not None:
            print("YES")
            get_region_data = Mbr.Member()
            stylelist = None

            if c_style == 'A':
                stylelist = get_region_data.select_all("SELECT distinct(a.type) FROM travel.attraction as a;")
            elif c_style == 'H':
                stylelist = get_region_data.select_all("SELECT distinct(a.type) FROM travel.hotel as a;")
            elif c_style == 'R':
                stylelist = get_region_data.select_all("SELECT distinct(a.type) FROM travel.restaurant as a;")
            else:
                stylelist = get_region_data.select_all("SELECT distinct(a.type) FROM travel.attraction as a;")

            print(json.dumps(stylelist))
            response = json.dumps({"Reglist" : stylelist})
            return HttpResponse(response, content_type='application/json')

    return HttpResponse("HI")