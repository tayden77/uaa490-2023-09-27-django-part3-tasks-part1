from django import forms

class NewTaskForm(forms.form):
    task = forms.CharField(label="New Task", min_length=5)
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=3, initial=1)

    def clean(self):
        super(NewTaskForm, self.clean())

        t = self.cleaned_data('task')
        p = self.cleaned_data('priority')

        if p >= 4 and len(t) < 10:
            self._errors['task'] = self.error_class([
                'Minimum 10 chars needed when priority >= 4'
            ])
        return self.cleaned_data