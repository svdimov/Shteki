import os

from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static
from django.db import models

# Create your models here.


from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from accounts.choices import GenderChoice
from accounts.managers import AppUserManager
from accounts.validators import FileSizeValidator


class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"

    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    failed_login_attempts = models.PositiveIntegerField(
        default=0,
    )

    is_locked = models.BooleanField(
        default=False,
    )
    account_locked_until = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
    )
    objects = AppUserManager()


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to='shteki',  #or cloudinaryFileField
        blank=True,
        null=True,
        validators=(FileSizeValidator(max_size_mb=5),)
    )

    gender = models.CharField(max_length=15, choices=GenderChoice)

    city = models.CharField(max_length=25, blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name or ''}  {self.last_name or ''}"

    @property
    def profile_picture_or_default(self):
        if self.profile_picture and self.profile_picture.storage.exists(self.profile_picture.name):
            return self.profile_picture.url
        return static('/images/2133123.jpg')

    def save(self, *args, **kwargs):
        try:
            this = Profile.objects.get(pk=self.pk)
            if this.profile_picture and this.profile_picture != self.profile_picture:

                old_path = this.profile_picture.path
                if os.path.isfile(old_path):
                    os.remove(old_path)
        except Profile.DoesNotExist:
            pass
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user.email})" if self.first_name or self.last_name else self.user.email
