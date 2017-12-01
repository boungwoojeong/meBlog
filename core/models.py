from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
   title = models.CharField(max_length=128)
   content = models.TextField()
   author = models.ForeignKey(User)
   create_at = models.DateTimeField(auto_now_add=True)
   update_at = models.DateTimeField(auto_now_add=True)

   #def __repr__(self):
   #      return 'sss'