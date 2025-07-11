from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class FileSizeValidator:
    def __init__(self, max_size_mb=5):
        self.max_size = max_size_mb * 1024 * 1024
        self.max_size_mb = max_size_mb

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError(
                f"File size must be under {self.max_size_mb} MB (currently {value.size / (1024 * 1024):.2f} MB)."
            )
