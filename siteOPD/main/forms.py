from .models import Task
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "task"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }