import json
from django import forms
from .models import Form, Question

class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['title', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_type', 'label', 'options', 'order']

    def clean_options(self):
        options = self.cleaned_data.get('options', '')
        try:
            json.loads(options)
        except json.JSONDecodeError:
            raise forms.ValidationError("Options must be valid JSON for dropdown or checkbox questions.")
        return options