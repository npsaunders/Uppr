from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


# class Category(models.Model):
#     name = models.CharField(blank=True,max_length=75)

#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return reverse('categories_detail', kwargs={'pk': self.pk})


class Question(models.Model):
    user_question = models.TextField()
    answer1 = models.CharField(blank=True,max_length=100)
    answer2 = models.CharField(blank=True,max_length=100)
    answer3 = models.CharField(blank=True,max_length=100)
    answer4 = models.CharField(blank=True,max_length=100)
    correct_answer = models.TextField()
    time_allowed = models.PositiveIntegerField()
    # Add FK linking user to the questions the user created
    # On delete, the user's question data will be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # categories = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    # changes to instance methods do not require re-generation / running of migrations
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'question_id': self.id})
