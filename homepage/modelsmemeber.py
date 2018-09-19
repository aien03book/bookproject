from django.db import connection

class member():
    def all(self):
        with connection.cursor() as cursor
        sql="select * from members"
        cursor.execute(sql,)
    def singel(self):
        pass
    def create(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass