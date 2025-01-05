# form_app/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Form, Question, Response
from .forms import FormForm, QuestionForm
from django.shortcuts import render, get_object_or_404

def create_form(request):
    if request.method == 'POST':
        form_form = FormForm(request.POST)
        if form_form.is_valid():
            form = form_form.save()
            return redirect('add_question', form_id=form.id)
    else:
        form_form = FormForm()
    return render(request, 'form_app/create_form.html', {'form': form_form})

def add_question(request, form_id):
    form = Form.objects.get(id=form_id)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid() and form.questions.count() < 100:
            question = question_form.save(commit=False)
            question.form = form
            question.save()
            return redirect('add_question', form_id=form_id)
    else:
        question_form = QuestionForm()
    return render(request, 'form_app/add_question.html', {'form': question_form, 'form_id': form_id})

def view_forms(request):
    forms = Form.objects.all().order_by('id')
    return render(request, 'form_app/view_forms.html', {'forms': forms})

def submit_form(request, form_id):
    form = Form.objects.get(id=form_id)
    if request.method == 'POST':
        data = {q.id: request.POST.get(str(q.id)) for q in form.questions.all().order_by('order')}
        Response.objects.create(form=form, data=data)
        return JsonResponse({"message": "Form submitted successfully!"})
    return render(request, 'form_app/submit_form.html', {'form': form})

def view_analytics(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    responses = form.responses.all()
    analytics = {
        'total_responses': responses.count(),
    }
    return render(request, 'form_app/analytics.html', {'form': form, 'analytics': analytics})

def view_form(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    return render(request, 'form_app/view_form.html', {'form': form})

def home(request):
    return redirect('view_forms') 