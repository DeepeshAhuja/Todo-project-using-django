from django.shortcuts import render, redirect
from new_app.models import TodoList

# Create your views here.
def home(request):
    
    tasks = TodoList.objects.all()

    if request.method == 'POST':
        new_task = request.POST.get('new_task')
        priority = request.POST.get('priority')
        task = TodoList(task_name=new_task, priority=priority)
        task.save()
    
    context = {'tasks': tasks}
    
    return render(request, 'index.html', context)
