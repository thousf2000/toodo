from django.shortcuts import render, redirect
from . models import task
from .forms import toddoform
# Create your views here.
def home(request):
    Task=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        date=request.POST.get('date','')
        priority=request.POST.get('priority','')
        TAST=task(name=name,priority=priority,date=date)
        TAST.save()
    return render(request,'home.html',{'Task':Task})

def delete(request,taskid):
    Task=task.objects.get(id=taskid)
    if request.method == 'POST':
        Task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    Task=task.objects.get(id=id)
    f=toddoform(request.POST or None,instance=Task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html', {'f':f,'task':task})
