from django.db import models

class Ticker(models.Model):
    name = models.CharField(max_length=7)
    sector = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
