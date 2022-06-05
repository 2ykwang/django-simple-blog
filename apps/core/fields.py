from django.db import models
import uuid


class UUIDImageField(models.ImageField):
    def generate_filename(self, instance, filename):
        uuid4 = uuid.uuid4()
        name = f"{uuid4}_{filename}"
        return super().generate_filename(instance, name)
