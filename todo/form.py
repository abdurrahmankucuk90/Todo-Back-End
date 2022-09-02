from django import forms
from django.forms import fields
from .models import Todo


class Todo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
