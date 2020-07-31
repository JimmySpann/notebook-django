from django import forms
from .models import Note

# Note Form
class NoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['title', 'body' ]
