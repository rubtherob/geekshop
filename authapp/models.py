from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
#from authapp.Validators.Validators import validate_login_title


class User(AbstractUser):
    image = models.ImageField(upload_to='user_image', blank=True)
    age = models.PositiveIntegerField(default=18)
 #   username = models.CharField(validators=[validate_login_title],unique=True,max_length=15)