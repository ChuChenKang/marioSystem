from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bot (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    icon = models.ImageField(upload_to='image/')
    createBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name