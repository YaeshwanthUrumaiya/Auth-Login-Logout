from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Give email when creating user")
        if not password: 
            raise ValueError("Give password when creating user")
        email = self.normalize_email(email)
        user = self.model(email = email)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("Give email when creating user")
        if not password: 
            raise ValueError("Give password when creating user")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save() 
        return user
    
class testmodel(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    no_stuff_done = models.IntegerField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()
    