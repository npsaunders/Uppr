# from sre_parse import CATEGORIES
from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    name = models.CharField(max_length=50)    
    screen_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(blank=True)
    email = models.CharField(blank=True, max_length=50)
    # Add FK linking user to the questions the user created
    # On delete, the user's question data will be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
       
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('profiles_detail', kwargs={'pk': self.id})

# # Define the categories
# CATEGORIES = (    
#     ('U', 'Uncategorized'),
#     ('B', 'Behavioral'),
#     ('LF', 'Language-Frontend'),
#     ('LB', 'Language-Backend'),
#     ('FF', 'Frameworks-Frontend'),
#     ('FB', 'Frameworks-Backend'),
#     ('D', 'Data Structures'),
#     ('A', 'Algorithms'),
# )


class Question(models.Model):
    user_question = models.TextField()
    answer1 = models.CharField(blank=True,max_length=100)
    answer2 = models.CharField(blank=True,max_length=100)
    answer3 = models.CharField(blank=True,max_length=100)
    answer4 = models.CharField(blank=True,max_length=100)
    correct_answer = models.TextField()
    category = models.CharField(max_length=50)
    time_allowed = models.PositiveIntegerField()
    # Add FK linking user to the questions the user created
    # On delete, the user's question data will be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    # category = models.CharField(
    #     max_length=2, 
    #     choices=CATEGORIES, 
    #     default=CATEGORIES[0][0])
    # changes to instance methods do not require re-generation / running of migrations
    def __str__(self):
        return self.user_question
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'question_id': self.id})


