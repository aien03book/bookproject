from django.db import connection

class Book():
    def all(self):
        with connection.cursor() as cursor:
            sql = """select * from bookpool"""
            cursor.execute(sql)
            books = cursor.fetchall()
        return books
    def serach(self,bookname):
        with connection.cursor()as cursor:
            sql ="""select * from bookpool where bookname=%s """
            cursor.execute(sql,(bookname,))
            bookname = cursor.fetchall()
            return bookname
    
        
        