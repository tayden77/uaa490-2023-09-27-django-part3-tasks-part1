from django import forms

class NewTaskForm(forms.form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10, initial=0)