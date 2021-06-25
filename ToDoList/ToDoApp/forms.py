from django import forms
from django.forms import ModelForm

from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'date_picker']
        widgets = {
            'date_picker': DateInput(attrs={'placeholder': 'yyyy-mm-dd'}),
        }

class TaskForm1(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'date_picker', 'complete']
        widgets = {
            'date_picker': DateInput(),
        }