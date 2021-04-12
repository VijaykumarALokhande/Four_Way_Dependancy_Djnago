from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
