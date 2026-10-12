from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=2555, unique=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=255)
    introduction = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)


    def __str__(self):
        return self.comment





