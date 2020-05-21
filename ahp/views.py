from django.shortcuts import render, redirect, get_object_or_404
from .forms import *


# Create your views here.
def add_crit_model(request):
    if request.method == "POST":
        form = Crit_model_form(request.POST)
        if form.is_valid():
            crit_model = form.save(commit=False)
            crit_model.save()
            return redirect('crit_model_details', pk=crit_model.pk)
    else:
        form = Crit_model_form()
    return render(request, 'ahp/add_crit_model.html', {'form': form})


def welcome(request):
    models = Crit_model.objects.order_by('-id')
    return render(request, 'ahp/welcome.html', {'models': models})


def crit_model_details(request, pk):
    criteria = Criteria.objects.filter(crit_model=pk).first()
    elements = Element.objects.filter(crit_model=pk).order_by('id')
    return render(request, 'ahp/crit_model_details.html', {'criteria': criteria, 'pk': pk, 'elements': elements})


def modify_criterias(request, pk):
    try:
        criteria = Criteria.objects.get(crit_model_id=pk)
        if request.method == "POST":
            form = Criteria_form(request.POST, instance=criteria)
            if form.is_valid():
                criteria = form.save(commit=False)
                criteria.crit_model_id = pk
                criteria.save()
                return redirect('crit_model_details', pk=pk)
        else:
            form = Criteria_form(instance=criteria)
    except:
        if request.method == "POST":
            form = Criteria_form(request.POST)
            if form.is_valid():
                criteria = form.save(commit=False)
                criteria.crit_model_id = pk
                criteria.save()
                return redirect('crit_model_details', pk=pk)
        else:
            form = Criteria_form()

    return render(request, 'ahp/modify_criterias.html', {'form': form})


def modify_elements(request, pk):
    elements = Element.objects.filter(crit_model_id=pk).order_by('id')
    if request.method == "POST":
        form = Element_form(request.POST, request.FILES)
        if form.is_valid():
            element = form.save(commit=False)
            element.crit_model_id = pk
            element.save()
            return redirect('modify_elements', pk=pk)
    else:
        form = Element_form()
    return render(request, 'ahp/modify_elements.html', {'form': form, 'elements': elements})


def solve(request,pk):
    return render(request, 'ahp/solve.html')