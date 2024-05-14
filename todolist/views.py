from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import Tasklist
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

def index(request):
    context = {
        'index_text':"welcome to the index page,",
    }
    return render(request,"index.html",context)



def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("New Task Added!"))
            return redirect('todolist')
    else:
        all_tasks = Tasklist.objects.all()
        paginator = Paginator(all_tasks, 8)
        page_number = request.GET.get('pg')
        paginated_tasks = paginator.get_page(page_number)
        return render(request, "todolist.html", {'all_tasks': paginated_tasks})
    



def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.delete()  
    return redirect("todolist")



def edit_task(request,task_id):
    if request.method == "POST":
            task = Tasklist.objects.get(pk=task_id)
            form = TaskForm(request.POST or None,instance= task)
            if form.is_valid():
                form.save()
            
        
            messages.success(request,("Task Edited!"))
            return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request,"edit.html",{'task_obj':task_obj})
    
def complete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = True  
    task.save()

    return redirect("todolist")

def pending_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False 
    task.save()

    return redirect("todolist")
    
def about(request):
    context = {
        'about_text':"welcome to about manager!.",
        }
    return render (request,"aboutus.html",context)



def contact(request):
    context = {
        'contact_text':"welcome to contact manager!.",
        }
    return render(request,"contact.html",context)

