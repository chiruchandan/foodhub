from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class usermanager(BaseUserManager):
    def create_user(self,username,first_name,last_name,email,password=None):
        if not email:
            raise ValueError("user must contain email")
        if not username:
            raise ValueError("user must contain username")
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,first_name,last_name,email,password=None):
         user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
         self.is_admin=True
         self.is_staff=True
         self.is_superuser=True
         self.is_active=True
         self.save(using=self._db)
         return user
    
class User(AbstractBaseUser):
    vendor=1
    customer=2

    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

    #extra fields
    date_joineed=models.DateField(auto_now_add=True)
    last_modified=models.DateField(auto_now_add=True)
    create_date=models.DateField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']
    objects=usermanager()

    def __str__(self):
        return self.email


         