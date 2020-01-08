from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

