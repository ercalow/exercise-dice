from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from diceApp.models import Exercise
from django.urls import reverse_lazy
# You have to use reverse_lazy when doing generic views
import random

# Create your views here.
class ExerciseListView(ListView):
    model = Exercise

class ExerciseDetailView(DetailView):
    model = Exercise

class ExerciseCreateView(CreateView):
    model = Exercise
    fields = ('name', 'muscleGroup', 'muscleGroup2', 'difficulty', 'reps', 'alwaysInclude')
    # fields you want to insert. Don't need to do ID - automatic

class ExerciseUpdateView(UpdateView):
    model = Exercise
    fields = ('name', 'muscleGroup', 'muscleGroup2', 'difficulty', 'reps', 'alwaysInclude',)
    # you can restrict the update-able stuff to only certain fields
    # ya need the comma and yes it's a tuple???

class ExerciseDeleteView(DeleteView):
    model = Exercise
    success_url = reverse_lazy('home')
    # the name of the view where django should send the user next.
    # it's like what we did in the model, but doesn't make sense to put it there.
    # it should match the 'name='' in the url for the view.

def generateWorkout(request):
    #allExercises = Exercise.objects.order_by('?')
    numExercises = 10
    allExercises = Exercise.objects.order_by('?')[0:numExercises]

    return render(request, 'diceApp/workout.html', {'exercises':allExercises})
