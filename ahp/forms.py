from django import forms

from .models import *


class Crit_model_form(forms.ModelForm):
    class Meta:
        model = Crit_model
        fields = ('name',)


class Criteria_form(forms.ModelForm):
    class Meta:
        model = Criteria
        fields = ('crit1', 'crit2', 'crit3',)


class Element_form(forms.ModelForm):
    class Meta:
        model = Element
        fields = ('name', 'attrib1', 'attrib2', 'attrib3', 'image',)
        labels = {
            "name": "Nazwa",
            "attrib1": "Nazwa",
            "attrib2": "Nazwa",
            "attrib3": "Nazwa",
            "image": "Wygląd",
        }
