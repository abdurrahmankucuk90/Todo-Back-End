from pydoc import describe
from django.db import models


status_choices = [
    ('C', 'Completed'),
    ('P', 'Pending'),
    ('I', 'In-Progres'),
]
priority_choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),    
]
#!Emoji windowsKey + .
# Create your models here.
class Todo(models.Model):
    title = models.CharField("title", max_length=50)
    describtion = models.TextField("description")
    status = models.CharField( max_length=2, choices = status_choices)
    priority = models.CharField(max_length=2, choices= priority_choices)
    created_data = models.DateTimeField( auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
 
 
    def __str__(self):
        return f'priority: {self.priority} {self.title} - {self.status}'
    
    class Meta:
        ordering = ["priority"]



 