from django.db import connection

class MR:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from meetingrooms")
            datas = cursor.fetchall()
        return datas

