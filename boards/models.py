from django.db import models

# Create your models here.
class Members(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=45)
    age = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'members'


class Board(models.Model):
    boardid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'boards'    


class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    message = models.TextField(max_length=4000)
    board = models.ForeignKey('Board',models.DO_NOTHING,db_column='boardid')
    createdat = models.DateTimeField(auto_now_add=True)
    createdby = models.ForeignKey('Members',models.DO_NOTHING,db_column='memberid')
    
    class Meta:
        db_table = 'posts'       