from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps_cooking = models.TextField()
    time_for_cooking = models.IntegerField(default=10)
    photo = models.ImageField(upload_to="img/%Y/%m/%d/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    