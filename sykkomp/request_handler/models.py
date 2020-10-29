from django.db import models

# Create your models here.
class CycleTimes(models.Model):
    last_data = models.CharField(max_length=200)

    def __str__(self):
        return self.last_data