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

    def ad(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select time,addr from restaurant where resid=%s",(id,))
            data2 = cursor.fetchone()
        return data2

    def resid(self):
        with connection.cursor() as cursor:
            cursor.execute("select TripID from itinerary")
            data3 = cursor.fetchone()
        return data3

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