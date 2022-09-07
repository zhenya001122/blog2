from django.db import models

from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               default='id user',
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='posts')
    title = models.CharField(max_length=200, help_text="Введите заголовок")
    slug = models.SlugField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Post: {self.title}, {self.text}"

class Tag(models.Model):
    title = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post)

class Address(models.Model):
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
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"Phone: {self.phone}\n"
