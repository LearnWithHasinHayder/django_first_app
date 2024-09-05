from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date=models.DateField(null=True, blank=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks", default=1)