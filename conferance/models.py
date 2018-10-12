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


#會議室modle
class ConfeRoom(models.Model):
    num = models.CharField(max_length=5)
    img = models.CharField(max_length=45)
    class MEAT:                 
        ordering = ["num"]
    def __str__(self):
        return self.num


#預約狀況
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Members', on_delete=models.CASCADE,db_column='user_id')
    room = models.ForeignKey('ConfeRoom', on_delete=models.CASCADE,db_column='room_id')
    time = models.DateField()

    def __str__(self):
        return str(self.user)