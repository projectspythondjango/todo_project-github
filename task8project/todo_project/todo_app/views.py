from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from .forms import TodoForm
# Create your views here
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Tasklist(ListView):
    model=Task
    template_name='home.html'
    context_object_name='key1'
class Taskdetail(DetailView):
    model=Task
    template_name='details.html'
    context_object_name='task'
class Taskupdate(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task'

    def get_success_url(self):
        return reverse_lazy('detailpage',kwargs=[{'pk':self.object.id}])
class  Taskdelete(DeleteView):
    model=Task
    template_name='delete.html'
    success_url= reverse_lazy('todo_app:cbvhome')


def add1(request):
    task1=Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority1=request.POST.get('priority','')
        date1=request.POST.get('date','')
        task=Task(name=name,priority=priority1,date=date1)
        task.save()
    return render(request,"home.html",{'key1':task1})
# def details(request):
#     task1=Task.objects.all()
#     return render(request,"details.html",{'key1':task1})
def delete(request,task_id):
    task2=Task.objects.get(id=task_id)
    if request.method=="POST":
        task2.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,id):
    task3=Task.objects.get(id=id)
    form2=TodoForm(request.POST or None,instance=task3)
    if form2.is_valid():
        form2.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form2,'task':task3})

