from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import modelsres
# from . import modelsproduct
from .modelsres import bookingq
import datetime
import random


def hotel(request):
    id_hotel=request.GET["hoid"]
    # id_hotel="60000"
    bk = modelsres.bookingq() #modelsproduct.Product()
    data = id_hotel
    print(data)
    print("-------")
    t = bk.simg(data)
    print("-----")
    imgsrc = t[0]
    print(imgsrc)
    ##抓detail
    d = bk.detail(data)
    # detail = 
    print("d::::::::::::::::::::::::::::",d)
    dname=d[0]
    # 飯店名稱
    dtype=d[1]
    #飯店type
    # dtel=d[1]
    ad = bk.ad(data)
    #抓timeaddr
    print(ad)
    dstyle=ad[0]
    #房型
    dstyle1=ad[1]
    #房型
    dprice=ad[2]
    #價錢
    dprice1=ad[3]  


   
   
   
    print('-------------------------------------------------HI1')

    if request.method=="GET":
        request.session['hoid'] = request.GET['hoid']
        request.session.modified = True
        print('+++++++++'+request.GET['hoid'])

    #Check for login
    isFooterShow=False
    if 'user' in request.session:
        useris = request.session['user']
        isLogin = True
    else:
        return redirect('../member/')
   
    
    if request.method == "POST":


        # print("---------------------------------------")
        #上傳檔案
        # myFile = request.FILES["ProductImage"]
        # fs = FileSystemStorage()
        # fs.save(myFile.name, myFile)
        
        #取得表單透過POST傳過來的資料
        print('-------------------------------------------------HI')
        horder_tel = request.POST['htel']
        horder_name = request.POST['hname']
        horder_date = request.POST['daterange']
        
        print('-------------------------------------------------')
        print(horder_tel,horder_name,horder_date)
        print('-------------------------------------------------')
        # UnitCost = request.POST['UnitCost']
        horder_id = random.randint(60000,69999)
        # CategoryID = request.POST['CategoryID']
        # ProductImage = myFile.name
        Resid='10'
        MEMBER_ID='100370'
        NumberOfPeople='20'

        id_hotel = None
        if 'hoid' in request.session:
            id_hotel = request.session['hoid']
        else:
            id_hotel = '60000'

        #todo 把資料寫進資料庫
        bk = modelsres.bookingq() #modelsproduct.Product()
        data = tuple([horder_id,horder_date,horder_name,horder_tel,id_hotel,MEMBER_ID])
        print(data)
        bk.create(data)
       
        # return redirect('/product')
        
    #GET
    #回傳一個網頁，讓使用者可以輸入資料
    # category = modelsres.Category()
    # datas = category.all()
    # print(datas)  #((),(),())
    return render(request,'hotel/hotel.html',locals())

