from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.notes, name='notes'),
    path('notes/<int:note_id>', views.note_details, name='note_details'),
    path('notes/<int:note_id>/edit', views.note_edit, name='note_edit'),

]
