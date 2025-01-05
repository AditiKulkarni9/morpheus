# form_app/models.py

from django.db import models
import json

class Form(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = (
        ('text', 'Text'),
        ('dropdown', 'Dropdown'),
        ('checkbox', 'Checkbox'),
    )
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    label = models.CharField(max_length=255)
    options = models.TextField(blank=True, null=True)  # JSON or comma-separated for dropdown/checkbox
    order = models.PositiveIntegerField(default=0, help_text="Order of the question in the form")

    def get_options(self):
        if self.options:
            return json.loads(self.options)
        return []

    def __str__(self):
        return self.label

class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='responses')
    data = models.JSONField()  # JSON structure to hold responses

    def __str__(self):
        return f"Response for {self.form.title}"