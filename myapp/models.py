from django.conf import settings
from django.db import models

class MyApp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)