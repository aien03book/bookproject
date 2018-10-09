from django.db import connection

class Book:
    #讀出category所有資料
    def cateall(self):
        with connection.cursor() as cursor:
            sql = """select * from bookcate order by bookcate"""
            cursor.execute(sql)
            cates = cursor.fetchall()
        return cates

    #讀出所有資料
    def all(self):
        with connection.cursor() as cursor:
            sql = """select * from bookpool"""
            cursor.execute(sql)
            books = cursor.fetchall()
        return books

    #讀出單筆資料
    def single(self, id):
        with connection.cursor() as cursor:
            sql = """select * from bookpool where id=%s"""
            #tuple
            cursor.execute(sql,(id,))
            book = cursor.fetchone()
        return book

    #新增資料    
    def create(self, book):
        with connection.cursor() as cursor:
            sql = """insert into bookpool(bookid,bookcate,bookname,author,issuedate,buydate,whoissue,bookimg01)
                     values(%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, book)

    def update(self, book):
        with connection.cursor() as cursor:
            sql = """update bookpool set bookname=%s,author=%s,issuedate=%s,buydate=%s,whoissue=%s
                     where id=%s"""
            cursor.execute(sql, book)

    def updateimg(self, book):
        with connection.cursor() as cursor:
            sql = """update bookpool set bookimg01=%s
                     where id=%s"""
            cursor.execute(sql, book)

    def delete(self, id):
        with connection.cursor() as cursor:
            sql = """delete from bookpool where id=%s"""
            cursor.execute(sql,(id,))