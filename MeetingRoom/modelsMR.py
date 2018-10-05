from django.db import connection

class MR:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from meetingrooms")
            datas = cursor.fetchall()
        return datas
    def single(self, id):
        with connection.cursor() as cursor:
            sql = """select * from meetingrooms where id=%s"""
            #tuple
            cursor.execute(sql,(id,))
            data = cursor.fetchone()
        return data