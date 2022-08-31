from django.db import models
from django.conf import settings

class Addres(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="address"
    )
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    house_number = models.CharField(max_length=20)
    phone = models.CharField(
        max_length=12,
        help_text='Введите в формате 375*********'
    )

    def __str__(self):
        return f"Phone: {self.phone}\n"