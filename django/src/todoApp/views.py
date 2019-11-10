from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from todoApp.models import Todo
from todoApp.forms import TodoForm

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todoApp/todo_list.html', {'todos':todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == "POST":
        todo.switch_finish()
    return render(request, 'todoApp/todo_detail.html', {'todo':todo})

def todo_new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()            
            return redirect('todo_detail', id=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todoApp/todo_edit.html', {'form':form})

def todo_edit(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_detail', id=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todoApp/todo_edit.html', {'form':form})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todoApp/todo_delete.html', {'todo':todo})
    


