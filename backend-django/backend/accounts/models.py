from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class User(AbstractUser):
  flag = models.IntegerField(blank=True, default=1)
  username = None
  email = models.EmailField(_('email address'), unique=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager()


  
  def __str__(self):
      return self.email

# Create your models here.
