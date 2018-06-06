from django.db import connection

class bookingq:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from products")
            datas = cursor.fetchall()
        return datas
    
    def simg(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select imgsrc from hotel where id_hotel=%s",(id,))
            data = cursor.fetchone()
        return data

    def detail(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select title,type from hotel where id_hotel=%s",(id,))
            data1 = cursor.fetchone()
        return data1
    

    def Hname(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select title from hotel where id_hotel=%s",(id,))
            data5 = cursor.fetchone()
        return data5

    

    def ad(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select style,style1,h_price,h_price1 from travel.hotel where id_hotel=%s",(id,))
            data2 = cursor.fetchone()
        return data2

    def id_hotel(self):
        with connection.cursor() as cursor:
            cursor.execute("select TripID from itinerary")
            data3 = cursor.fetchone()
        return data3
    def atdid(self):
        with connection.cursor() as cursor:
            cursor.execute("select Attracid from itinerary_day where idday = %s",(day,))
            data6 = cursor.fetchone()
        return data6

    def hotelid(self,day):
        with connection.cursor() as cursor:
            cursor.execute("select Hotno from itinerary_day where idday = %s",(day,))
            data6 = cursor.fetchone()
        return data6

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
            sql = """insert into horder(horder_id,horder_date,horder_name,horder_tel,id_hotel,MEMBER_ID)
                            values(%s,%s,%s,%s,%s,%s)"""
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

