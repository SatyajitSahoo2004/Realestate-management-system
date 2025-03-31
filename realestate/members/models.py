from django.db import models

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=100, default="")
    role = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=3)

    def _str_(self):
        return self.name