from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.TextField()
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True)

    def switch_finish(self):
        self.is_finished = not self.is_finished
        self.save()
    
    def __str__(self):
        return self.title
    
