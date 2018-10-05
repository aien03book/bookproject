from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    last_modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "todo"