from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
   title = models.CharField(max_length=256)
   text =  models.TextField()
   date = models.DateTimeField(default=timezone.now)
   published_date = models.DateTimeField(blank=True, null=True)
   author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

   def __str__(self):
      return self.title

   