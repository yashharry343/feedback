from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=30)  
    roll_no = models.CharField(max_length=10)  
    contact = models.CharField(max_length=15) 
    email = models.EmailField(unique=True)  
    feedback = models.TextField()  

    def __str__(self):
        return f'Feedback from {self.name}'