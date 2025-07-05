from django.db import models
from django.contrib.auth.models import User

class manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # link task to a user
    title = models.CharField(max_length=255)                 # task title
    completed = models.BooleanField(default=False)           # task status
    created = models.DateTimeField(auto_now_add=True)        # creation timestamp

    def __str__(self):
        return self.title

# Create your models here.
