from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=512)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
