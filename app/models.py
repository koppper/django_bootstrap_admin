from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from app.managers import CustomUserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    middle_name = models.CharField(max_length=155, null=True, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_author = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Speakers(models.Model):
    name = models.CharField(max_length=100)
    employee = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to="img/", blank=True, null=True)
    social_media = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Speaker'
        verbose_name_plural = 'Speakers'


