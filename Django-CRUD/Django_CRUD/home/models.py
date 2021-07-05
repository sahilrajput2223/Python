from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=50)
    email = models.EmailField()
    mobileNumber = models.CharField(max_length=10)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.userName