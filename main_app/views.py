from django.shortcuts import HttpResponse, render, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.
def home(request):
    return redirect('notes')

def notes(request):
    notes = Note.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, 'note-list.html', context)
 

def note_details(request, note_id):
    note = Note.objects.get(id=note_id)
    note_form = NoteForm()
    context = {
        'note': note,
        'note_form': note_form
    }
    return render(request, 'note-details.html', context)

def note_edit(request, note_id):   
    note = Note.objects.get(id=note_id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_details', note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note-edit.html', {'note': note, 'form': form})