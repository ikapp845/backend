from django.db import models
import uuid
from datetime import datetime
from django.utils.translation import gettext_lazy as _
import random
import string
from django.contrib.auth.models import User



def key_generator():
    key = ''.join(random.choice(string.digits) for x in range(6))
    return key
    
class Profile(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE,null = True,blank = True)
  name = models.CharField(max_length = 200,null = True,blank = True)
  id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key = True)
  email = models.CharField(max_length = 200,null = True,blank = True)
  gender = models.CharField(max_length = 200,null = True,blank = True)
  paid_time = models.DateField(null=True, blank=True)
  paid = models.CharField(max_length = 200,default = "False")
  last_login = models.DateTimeField(default=datetime.now(),null = True,blank = True)
  image_url = models.ImageField(upload_to = "media/",null = True,blank = True)
  total_likes = models.IntegerField(null = True,blank = True,default=0)
  coins = models.IntegerField(default = 0)


  def __str__(self):
    return self.email

# Create your models here.
