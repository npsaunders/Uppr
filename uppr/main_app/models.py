from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

ANSWERS = (
    ('T', 'True'),
    ('F', 'False'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),

)

class Question(models.Model):
    user_question = models.TextField()
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    answer4 = models.CharField(max_length=100)
    time_allowed = models.PositiveIntegerField()
    # Add FK linking user to the questions the user created
    # On delete, the user's question data will be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # changes to instance methods do not require re-generation / running of migrations
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'question_id': self.id})
