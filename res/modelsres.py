from django.db import connection

class bookingq:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from products")
            datas = cursor.fetchall()
        return datas
    
    def simg(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select imgsrc from restaurant where resid=%s",(id,))
            data = cursor.fetchone()
        return data

    def detail(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select title,type,tel from restaurant where resid=%s",(id,))
            data1 = cursor.fetchone()
        return data1

#######用景點id抓名稱
    def atd(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select title from attraction where idAttraction=%s",(id,))
            data5 = cursor.fetchone()
        return data5

    def Hname(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select title from hotel where id_hotel=%s",(id,))
            data5 = cursor.fetchone()
        return data5


    def ad(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select time,addr from restaurant where resid=%s",(id,))
            data2 = cursor.fetchone()
        return data2
###從行程day抓id
    def resid(self,day):
        with connection.cursor() as cursor:
            cursor.execute("select Resid from itinerary_day where idday = %s",(day,))
            data3 = cursor.fetchone()
        return data3

    def atdid(self,day):
        with connection.cursor() as cursor:
            cursor.execute("select Attracid from itinerary_day where idday = %s",(day,))
            data6 = cursor.fetchone()
        return data6

    def hotelid(self,day):
        with connection.cursor() as cursor:
            cursor.execute("select Hotno from itinerary_day where idday = %s",(day,))
            data6 = cursor.fetchone()
        return data6    
###############################################################
################會員ID抓行程####################################
    def itine(self,id):
        with connection.cursor() as cursor:
            cursor.execute("select * from itinerary where idMember = %s",(id,))
            data6 = cursor.fetchone()
        return data6   


    def trip(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select * from travel.itinerary as A,travel.itinerary_day as B where A.TripID = B.TripID and A.TripID =%s",(id,))
            data4 = cursor.fetchall()
        return data4

    def create(self, bk):
        with connection.cursor() as cursor:
            sql = """insert into orders(Orderid,Resid,MEMBER_ID,BookingDate,NumberOfPeople,hotname,hottel)
                            values(%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, bk)
        
    def update(self, product):
        with connection.cursor() as cursor:
            sql = """update products set categoryid=%s, modelnumber=%s, modelname=%s,
                         unitcost=%s, productimage=%s, description=%s where productid=%s"""
            cursor.execute(sql,product)

    def delete(self, id):
        with connection.cursor() as cursor:
            sql = "delete from products where productid=%s"
            cursor.execute(sql,(id,))

#########################  #########################
    def country(self,id):
        with connection.cursor() as cursor:
            cursor.execute("select Countryname from country where idCountry = %s",(id,))
            data8 = cursor.fetchone()
        return data8

    def area(self,id):
        with connection.cursor() as cursor:
            cursor.execute("select Regionname from region where idRegion = %s",(id,))
            data9 = cursor.fetchone()
        return data9 


    
    # def CT(self,what,who,tab,id):
    #     with connection.cursor() as cursor:
    #         cursor.execute("select %s from %s where %s = %s",(what,who,tab,id,))
    #         data6 = cursor.fetchone()
    #     return data6
