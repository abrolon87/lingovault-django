from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."
