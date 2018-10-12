# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bookpool(models.Model):
    bookname = models.CharField(max_length=145)
    author = models.CharField(max_length=140)
    issuedate = models.DateField(blank=True, null=True)
    buydate = models.DateField(blank=True, null=True)
    publisher = models.CharField(max_length=30, blank=True, null=True)
    bookid = models.CharField(max_length=30, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=200, blank=True, null=True)
    bookimage = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookpool'


class Bookrecord(models.Model):
    terms = models.IntegerField(primary_key=True)
    borrowtime = models.CharField(max_length=100, blank=True, null=True)
    returntime = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=500, blank=True, null=True)
    bookid = models.ForeignKey(Bookpool, models.DO_NOTHING, db_column='bookid', blank=True, null=True)
    memberid = models.ForeignKey('Members', models.DO_NOTHING, db_column='memberid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookrecord'


class Members(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    age = models.CharField(max_length=45, blank=True, null=True)
    memberid = models.CharField(max_length=45, blank=True, null=True)
    joindate = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'members'
