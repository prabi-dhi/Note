from django.contrib.auth.models import User
from django.db import models
 
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associated each note with a user

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        ordering = ('title',)
        
    def __str__(self):
        return self.title 