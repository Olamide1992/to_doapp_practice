from django import forms
from .models import TodoApp


class TodoAppForms(forms):
    class Meta:
        model = TodoApp
        fields = [
            "title",
            "description"
        ]