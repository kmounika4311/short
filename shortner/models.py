from django.db import models
import string, random
from rest_framework import generics
from django.contrib.auth.models import User




class ShortUrl(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.url} :: {self.code}"
    
    def generate_code(self):
        """
        This function will generate 5 digit code.
        """
        code = ""
        data = string.ascii_letters + string.digits
        for i in range(5):
            code += data[random.randint(0, len(data)-1)]
        return code



# 1. Email Sender





