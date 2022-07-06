from datetime import datetime
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.name}'

class Todo(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField()
    due_date = models.DateField()
    due_time = models.TimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='todos')

    class Meta:
        ordering = ['due_date', 'due_time']

    def __str__(self):
        return f'{self.name}'
