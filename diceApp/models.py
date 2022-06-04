from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django import forms

# Create your models here.
class Exercise(models.Model):
    muscleOptions = [('abs', 'Abs'), ('push', 'Push'), ('pull', 'Pull'), ('legs', 'Legs')]
    difficultyOptions = [(1, '1'), (2, '2'), (3, '3')]
    includeOptions = [('No', 'No'), ('Yes', 'Yes')]

    name = models.CharField(max_length=30)
    muscleGroup = models.CharField(max_length=30, choices=muscleOptions)
    muscleGroup2 = models.CharField(max_length=30, choices=muscleOptions, blank=True)
    difficulty = models.IntegerField(choices=difficultyOptions)
    reps = models.IntegerField()
    alwaysInclude = models.CharField(max_length=30, choices=includeOptions)

    def get_absolute_url(self):
        # this tells the app where to go after the new thing is created.
        return reverse('home')
        # return reverse('detail', kwargs={'pk': self.pk})
        # 'detail' is the 'name='' of the view where it will return to.
        # pk will be the id of the thing.
