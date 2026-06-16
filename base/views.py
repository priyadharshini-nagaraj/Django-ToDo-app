from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    data = TaskModel.objects.all()
    return render(request,'home.html',{'data':data})

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        TaskModel.objects.create(
            task = title,
            desc = desc
        )
    return render(request,'add.html')

def completed(request):
    data = CompleteModel.objects.all()
    return render(request,'completed.html',{'data':data})

def trash(request):
    data = TrashModel.objects.all()
    return render(request,'trash.html',{'data':data})

def about(request):
    return render(request,'about.html')

def hcomplete(request,pk):
    data = TaskModel.objects.get(id=pk)
    CompleteModel.objects.create(
        task = data.task,
        desc = data.desc
    )
    data.delete()
    return redirect('home')

def hdelete(request,pk):
    data = TaskModel.objects.get(id=pk)
    TrashModel.objects.create(
        task = data.task,
        desc = data.desc
    )
    data.delete()
    return redirect('home')

def crestore(request,pk):
    data = CompleteModel.objects.get(id=pk)
    TaskModel.objects.create(
        task = data.task,
        desc = data.desc
    )
    data.delete()
    return redirect('completed')

def cdelete(request,pk):
    data = CompleteModel.objects.get(id=pk)
    TrashModel.objects.create(
        task = data.task,
        desc = data.desc
    )
    data.delete()
    return redirect('completed')

def trestore(request,pk):
    data = TrashModel.objects.get(id=pk)
    TaskModel.objects.create(
        task = data.task,
        desc = data.desc
    )
    data.delete()
    return redirect('trash')

def tdelete(request,pk):
    data = TrashModel.objects.get(id=pk)
    data.delete()
    return redirect('trash')