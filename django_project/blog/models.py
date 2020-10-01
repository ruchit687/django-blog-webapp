from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class post(models.Model):
    SrNo = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.SlugField(max_length = 200)
    timeStamp = models.DateTimeField(blank =  True)

    def __str__(self):
        return self.title + " by " + self.author
