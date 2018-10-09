# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from member.models import Members 


class Bookpool(models.Model):
    bookname = models.CharField(max_length=145)
    author = models.CharField(max_length=140)
    issuedate = models.DateField()
    buydate = models.DateField(blank=True, null=True)
    publisher = models.CharField(max_length=30)
    bookid = models.CharField(max_length=30, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=45)  # Field name made lowercase.
    description = models.CharField(max_length=200, blank=True, null=True)
    bookimage = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):  # 增加代码
        return self.bookname   # 增加代码
    class Meta:
        managed = False
        db_table = 'bookpool'
        

class Bookrecord(models.Model):
    terms = models.AutoField(primary_key=True)
    borrowtime = models.DateTimeField()
    returntime = models.DateTimeField()
    note = models.TextField()
    
    bookid = models.ForeignKey(Bookpool,models.DO_NOTHING,db_column='bookid')
    memberid = models.ForeignKey(Members,models.DO_NOTHING,db_column='memberid')
   
    class Meta:
        managed = False
        db_table = 'bookrecord'