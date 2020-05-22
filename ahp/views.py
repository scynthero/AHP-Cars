from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from pyahp import *
import json


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


def solve(request, pk):
    criteria = Criteria.objects.get(crit_model=pk)
    elements = Element.objects.filter(crit_model=pk)
    print(elements)
    return render(request, 'ahp/solve.html', {'criteria': criteria, 'pk': pk, 'elements':elements})


def solver(request, pk):
    response = request.POST.dict()
    response.pop('csrfmiddlewaretoken')
    # here we do matrix for criteria
    array = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    for entry in response:
        if int(response[entry]) < 0:
            array[int(entry[1])][int(entry[0])] = abs(int(response[entry]))
        else:
            array[int(entry[0])][int(entry[1])] = int(response[entry])
    for x in range(4):
        for y in range(4):
            if array[x][y] == 0:
                array[x][y] = 1/array[y][x]

    criteria = list(
        list(Criteria.objects.filter(crit_model=pk).values_list('crit1', 'crit2', 'crit3', 'crit4'))[0])
    alternatives = list(Element.objects.filter(crit_model=pk).values_list('name', flat=True))

    json_model = json.dumps({"name": "test", "method": "eigenvalue", "criteria": criteria, "subCriteria": {},
                             "alternatives": alternatives, "preferenceMatrices": {"criteria": array,
                                                                                  "alternatives:" + criteria[0]: [
                                                                                      'aaa'],
                                                                                  "alternatives:" + criteria[1]: [
                                                                                      'aaa'],
                                                                                  "alternatives:" + criteria[2]: [
                                                                                      'aaa'],
                                                                                  "alternatives:" + criteria[3]: [
                                                                                      'aaa'],
                                                                                  }})
    print(json_model)
    model = json.loads(json_model)
    ahp_model = parse(model)
    priorities = ahp_model.get_priorities()
    return redirect('crit_model_details', pk=pk)
