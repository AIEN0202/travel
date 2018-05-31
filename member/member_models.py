from django.db import connection

class Member:

    def excute_sql(self, sql, *parameter):
        print(parameter)
        with connection.cursor() as cs:
            rows =cs.execute(sql,parameter)
    
    def select_one(self, sql, *parameter):
        print(parameter)
        with connection.cursor() as cs:
            cs.execute(sql,parameter)
            rows = cs.fetchone()
        return rows

    def select_all(self, sql, *parameter):
        print(parameter)
        with connection.cursor() as cs:
            cs.execute(sql,parameter)
            rows = cs.fetchall()
        return rows