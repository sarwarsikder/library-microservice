from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    
    title = models.CharField(max_length=200)
    body = models.TextField()
    assign_to = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name="assign_to")
    assign_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name="assign_by")
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.title
