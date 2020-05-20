from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
def add_crit_model(request):
    if request.method== "POST":
        form = Crit_model_form(request.POST)
        if form.is_valid():
            crit_model = form.save(commit=False)
            crit_model.save()
            return redirect('crit_model_details', pk=crit_model.pk)
    else:
        form=Crit_model_form()
    return render(request, 'ahp/add_crit_model.html', {'form': form})

def welcome(request):
    models = Crit_model.objects.order_by('-id')
    return render(request, 'ahp/welcome.html', {'models':models})

def crit_model_details(request, pk):
    criteria = Criteria.objects.filter(crit_model=pk).first()
    return render(request, 'ahp/crit_model_details.html',{'criteria': criteria, 'pk':pk})


# TODO fix those functions below
def modify_criterias(request):
    if request.method== "POST":
        form = Criteria_form(request.POST)
        if form.is_valid():
            criteria = form.save(commit=False)
            criteria.save()
            return redirect('modify_criterias')
    else:
        form=Criteria_form()
    return render(request, 'ahp/modify_criterias.html', {'form': form})

def modify_elements(request):
    if request.method== "POST":
        form = Criteria_form(request.POST)
        if form.is_valid():
            element = form.save(commit=False)
            element.save()
            return redirect('modify_elements')
    else:
        form=Criteria_form()
    return render(request, 'ahp/modify_elements.html', {'form': form})

