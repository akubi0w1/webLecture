from django import forms
from todoApp.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body', 'deadline')
        widgets = {
            'deadline': forms.SelectDateWidget
        }