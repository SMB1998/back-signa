# brands/models.py

from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='in_process')  

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if self.name and self.owner:
            self.status = 'registered'
        else:
            self.status = 'in_process'
        super().save(*args, **kwargs)
