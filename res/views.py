
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import modelsres
# from . import modelsproduct
from .modelsres import bookingq
import datetime
import random
from member import member_models as Mbr

# Create your views here.
def res(request):
    ##用resid抓圖片src
    bk = modelsres.bookingq()

    if 'user' in request.session:
        useris = request.session['user']
        uid=("{}".format(useris[0]))
        isLogin = True
    else:
        print("NO GET")
        ########################
    teid = None

    if 'tripid' in request.session:
        teid = request.session['tripid']
    else:
        pass
        ########################
    IALL=bk.itine(uid,teid)
    ters=IALL[5]
    ######################
    Resid=request.GET["id"]
    # Resid=rid
    bk = modelsres.bookingq() #modelsproduct.Product()
    data = Resid
    print(data)
    t = bk.simg(data)
    imgsrc = t[0]
    print(imgsrc)
    ##抓detail
    d = bk.detail(data)
    # detail = 
    print(d)
    dname=d[0]
    dtype=d[1]
    dtel=d[2]
    ad = bk.ad(data)
    ##抓timeaddr
    print(ad)
    time=ad[0]
    addr=ad[1]
    # title="商品新增"
    # print(request.method);
    #POST
    if request.method == "POST" :
        print('GET POST ======================')


        # print("---------------------------------------")
        #上傳檔案
        # myFile = request.FILES["ProductImage"]
        # fs = FileSystemStorage()
        # fs.save(myFile.name, myFile)
        
        #取得表單透過POST傳過來的資料
        hottel = request.POST['uitel']
        hotname = request.POST['uiname']
        BookingDate = request.POST['bdaytime']
        print(hottel,hotname,BookingDate)
        print('-------------------------------------------------')
        # UnitCost = request.POST['UnitCost']
        Orderid = random.randint(51000,59999)
        # CategoryID = request.POST['CategoryID']
        # ProductImage = myFile.name

        MEMBER_ID=uid
        NumberOfPeople=ters
        #todo 把資料寫進資料庫
        bk = modelsres.bookingq() #modelsproduct.Product()
        data = tuple([Orderid,Resid,MEMBER_ID,BookingDate,NumberOfPeople,hotname,hottel])
        print(data)
        bk.create(data)
        oid=Orderid
        telon = hottel

        print("----------------------------------------------",oid,hottel,hotname)

    return render(request,'res/res.html',locals())

def booking(request):
    print('hi')
        ##用resid抓圖片src
    bk = modelsres.bookingq() #modelsproduct.Product()
    ##從行程day抓id
#     rid = bk.resid('1')
#     aid = bk.atdid('1')
#     hid = bk.hotelid('1')
#     # test = bk.CT(Countryname,country,idCountry,9001)
    
#     # print(rid)
#     # rid = rid[0]
# ##建list 拔/塞id
#         ####reslist
#     newlist=[]
#     for i in rid:
#         newlist.append(i.split('/'))

#     alist=[]
#     for i in aid:
#         alist.append(i.split('/'))  

#     hlist=[]
#     for i in hid:
#         hlist.append(i.split('/'))
        
# ####----------------加項11:30
#     print(alist)
#     print(hlist)

    teid = None

    if 'tripid' in request.session:
        teid = request.session['tripid']
    else:
        pass
    print(teid)
    # teid="700001"
    # trp = bk.trip(teid)
    # print(trp)
    # dname=d[0]
    # dtype=d[1]
    # dtel=d[2]

# ####newlist塞成dictiona
#     reidlist = newlist[0]

#     resdictlist = []

#     for item in reidlist:
#         print(item)
#         d = bk.detail(item)
#         resdictlist.append({'resid':item,'title':d[0]})
# #################################
# #####aid跟---------------------
#     Alist = alist[0]

#     Adictlist = []

#     for item in Alist:
#         print(item)
#         d = bk.atd(item)
#         Adictlist.append({'Aid':item,'Atitle':d[0]})

#     print(Adictlist)
# ####-------------------hid------
#     Hlist = hlist[0]

#     Hdictlist = []

#     for item in Hlist:
#         print(item)
#         d = bk.Hname(item)
#         Hdictlist.append({'Hid':item,'Htitle':d[0]})

#     print(Hdictlist)
#####################################
    if 'user' in request.session:
        useris = request.session['user']
        uid=("{}".format(useris[0]))
        isLogin = True
    else:
        print("NO GET")

#######################################
    # TRIP DATA
    IALL=bk.itine(uid,teid)
    print(IALL[2])
    tname=IALL[2]
    tday=IALL[3]
    print(tday)
    tdate=IALL[4]
    ters=IALL[5]
    tplc=IALL[6]
    tcountry=IALL[8]
    tarea=IALL[9]
    fcountry = (bk.country(tcountry)[0])
    farea = (bk.area(tarea)[0])
    print(fcountry)

    sign_data = Mbr.Member()
    triplist = sign_data.select_all("SELECT * FROM travel.itinerary_day where TripID = %s ;", teid)
    TOTAL_reslist = []
    
    for it in triplist:
        print(it)
        day = it[0]        
        hot = it[1]
        res = it[2]        
        attr = it[4]
        attrlist = []
        hotlist = []
        reslist = []
        print("RES{} HOT{} ATTR{}".format(res,hot,attr))
        if attr != '':
            for aitem in attr.split('/'):
                sel_name_data = Mbr.Member()
                a_name = sel_name_data.select_one('SELECT title FROM travel.attraction where idAttraction = %s;',aitem)
                # print('aaaaaaaaaaaaaaaaaaa')
                # print(a_name[0])
                # print('aaaaaaaaaaaaaaaaaaa')
                attrlist.append(a_name[0])
                attrlist.append({'getid':aitem,'getname':a_name[0]})
        else:
            attrlist = []

        if hot != '':
            for hitem in hot.split('/'):
                h_sel_name_data = Mbr.Member()                
                h_name = h_sel_name_data.select_one('SELECT title FROM travel.hotel where id_hotel = %s;',hitem)
                # print('hhhhhhhhhhhhhhhhhhhh')
                # print(h_name[0])
                # print('hhhhhhhhhhhhhhhhhhhh')
                # print(h_name[0])
                hotlist.append(h_name[0])
                hotlist.append({'getid':hitem,'getname':h_name[0]})
        else:
            hotlist = []

        if res != '':
            for ritem in res.split('/'):

                r_sel_name_data = Mbr.Member()
                r_name = r_sel_name_data.select_one('SELECT title FROM travel.restaurant where Resid = %s;',ritem)
                # print('rrrrrrrrrrrrrrrrrr')
                # print(r_name[0])
                # print('rrrrrrrrrrrrrrrrrrr')
                # reslist.append(r_name[0])
                reslist.append({'getid':ritem,'getname':r_name[0]})
        else:
            reslist = []

        TOTAL_reslist.append({'day':day,'attr':attrlist,'hot':hotlist,'res':reslist})

        print(day)
        print(attr)
        print(hot)
        print(res)
        print('')
    print(TOTAL_reslist)
    
    #--------------------------------------------MARK----------------------------------------------
# ##################################################################################################################
# ######################################################################################################################
#     print('AFTER itine')
#     cday=1
#     rei=1
#     rea=1
#     hea=1
#     Hdictlist1 = []
#     Adictlist1 = []
#     resdictlist1 = []
#     print('BEFORE WHILE')
#     while cday<=tday:
#         print('AFTER WHILE')
#         rid2 = bk.resid(cday)
#         aid2 = bk.atdid(cday)
#         hid2 = bk.hotelid(cday)
#         # print("HHH:",rid2,aid2,hid2)
#         cday += 1
# ######################################################################################################################
#         newlist1=[]
#         for i in rid2:
#             newlist1.append(i.split('/'))

#         alist1=[]
#         for i in aid2:
#             alist1.append(i.split('/'))  

#         hlist1=[]
#         print('===-----===')
#         print(hid2)
#         for i in hid2:
#             hlist1.append(i.split('/'))
            
#         # print(newlist1,alist1,hlist1)
#         print('////////////////////////////')
#         print(newlist1)
#         print('////////////////////////////')

#         ####newlist塞成dictiona
#         reidlist1 = newlist1[0]

#         # resdictlist1 = []
#         print('=======================')
#         print(reidlist1)
#         print('=======================')
#         for item in reidlist1:
#             residc = "resid"+str(rei)
#             # print(residc)
#             titlec = "title"+str(rei)
#             d = bk.detail(item)
#             resdictlist1.append({residc:item,titlec:d[0]})
            
#             rei += 1
#             print(resdictlist1)
#         #####景點###############
#         Alist1 = alist1[0]

#         # Adictlist1 = []

#         for item in Alist1:
#             Aidc = "Aid"+str(rea)
#             # print(hi)
#             Atitlec = "Atitle"+str(rea)
#             d = bk.atd(item)
#             print("hi")
#             Adictlist1.append({Aidc:item,Atitlec:d[0]})
            
#             rea += 1
#             print(Adictlist1)
#          ##########hotel#####################
#         Hlist1 = hlist1[0]

#         # Hdictlist1 = []
#         print("///////")
#         print(hlist1)

#         for item in Hlist1:
#             Hidc = "Hid"+str(hea)
#             # print(hi)
#             Htitlec = "Htitle"+str(hea)
#             d = bk.Hname(item)
#             print("hi")
#             Hdictlist1.append({Hidc:item,Htitlec:d[0]})
            
#             hea += 1
#             print(Hdictlist1)

    #--------------------------------------------MARK----------------------------------------------

    return render(request,'res/booking.html',locals())

def box(request):
# title = "res detail" 
    return render(request,'res/lightbox.html',locals())

    # Alist = alist[0]

    # Adictlist = []

    # for item in Alist:
    #     print(item)
    #     d = bk.atd(item)
    #     Adictlist.append({'Aid':item,'Atitle':d[0]})

    # print(Adictlist)