
from django.conf import settings
from django.core.validators import FileExtensionValidator


from django.db import models
from django.utils import timezone
from datetime import timedelta

from accounts.validators import FileSizeValidator
from events.choices import StatusChoice


class Event(models.Model):
    name = models.CharField(max_length=255)

    location = models.CharField(max_length=255)

    location_url = models.URLField(blank=True,null=True)

    description = models.TextField(blank=True, null=True)

    days = models.PositiveIntegerField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=StatusChoice,

    )
    start_date = models.DateField()

    city = models.CharField(max_length=100)



    image1 = models.ImageField(
        upload_to='event_images/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif']),
            FileSizeValidator(max_size_mb=6)
        ]
    )
    image2 = models.ImageField(
        upload_to='event_images/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif']),
            FileSizeValidator(max_size_mb=6)
        ]
    )
    image3 = models.ImageField(
        upload_to='event_images/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif']),
            FileSizeValidator(max_size_mb=6)
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_events',
        blank=True,
        null=True
    )



    def __str__(self):
        return self.name

    @property
    def end_date(self):
        """Calculate end date based on start_date and days"""
        if self.days:
            return self.start_date + timedelta(days=self.days)
        return self.start_date

    @property
    def is_past_event(self):
        """Determine if event is finished"""
        return self.end_date < timezone.now().date()
