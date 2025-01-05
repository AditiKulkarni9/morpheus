from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_form, name='create_form'),
    path('create/<int:form_id>/question/', views.add_question, name='add_question'),
    path('view/', views.view_forms, name='view_forms'),
    path('view/<int:form_id>/', views.view_form, name='view_form'),  # Assuming you have this view
    path('submit/<int:form_id>/', views.submit_form, name='submit_form'),
    path('analytics/<int:form_id>/', views.view_analytics, name='view_analytics'),
    path('', views.home, name='home'),
]