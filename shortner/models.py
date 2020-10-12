from django.db import models
import string, random


class ShortUrl(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=10)

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
