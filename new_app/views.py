from django.shortcuts import render, redirect
from new_app.models import TodoList

# Create your views here.
def home(request):
    
    tasks = TodoList.objects.all()
    context = {'tasks': tasks}
    
    return render(request, 'index.html', context)
