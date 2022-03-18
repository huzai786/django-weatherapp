from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created']
    