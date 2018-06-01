from django.db import connection

class Style:
    def all(self):
        with connection.cursor()as cursor:
            cursor.execute("select * from article")
            datas =cursor.fetchall()
        return datas

