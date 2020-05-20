from django import forms

from .models import *


class Crit_model_form(forms.ModelForm):

    class Meta:
        model = Crit_model
        fields = ('name',)

class Criteria_form(forms.ModelForm):

    class Meta:
        model = Criteria
        fields = ('crit1', 'crit2','crit3','crit4',)

class Element_form(forms.ModelForm):

    class Meta:
        model = Element
        fields = ('crit1', 'crit2','crit3','crit4', 'image',)