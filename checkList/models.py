from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    urgency = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tasks"
        ordering = ['urgency']

    def __str__(self):
        return self.title
