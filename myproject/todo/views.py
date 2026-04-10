from django.shortcuts import render, redirect
from .models import task

def todo(request):

    if request.method == "POST":
        title = request.POST.get('title')
        completed = request.POST.get('completed')

        
        task.objects.create(
                title=title,
                completed=True if completed else False
            )

        return redirect('/')

    tasks = task.objects.all()

    return render(request, 'todo.html', {
        'tasks': tasks
    })  
def delete_task(request, id):
    tasks_obj = task.objects.get(id=id)
    tasks_obj.delete()
    return redirect('/')

def update_task(request, id):
    task_obj = task.objects.get(id=id)

    if request.method == "POST":

        completed = request.POST.get('completed')

        task_obj.completed = True if completed else False

        task_obj.save()

    return redirect('/')

def edit_task(request, id):

    task_obj = task.objects.get(id=id)

    if request.method == "POST":

        new_title = request.POST.get('title')

        if new_title:
            task_obj.title = new_title
            task_obj.save()

        return redirect('/')

    return render(request, 'todo.html', {
        'task': task_obj
    })