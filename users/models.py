from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomManager(BaseUserManager):
    def create_user(self,username, email, password, **kwargs):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **kwargs)

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    objects = CustomManager()

    REQUIRED_FIELDS = ['email']