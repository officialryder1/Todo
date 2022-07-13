from django.shortcuts import render, redirect
from django import forms



class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')

def index(request):
    if "tasks" not in request.session:
        request.session['tasks'] = []
    return render(request, 'task/index.html', {'tasks': request.session['tasks']})

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task= form.cleaned_data["task"]
            request.session['tasks'] += [task]
            return redirect('home')
        else:
            return render(request, 'task/add.html', {'forms':form})

    return render(request, 'task/add.html', {'forms':NewTaskForm})