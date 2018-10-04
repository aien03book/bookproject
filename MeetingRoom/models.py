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
