from django.db import models

class Data(models.Model):
    text = models.CharField(max_length=300)
