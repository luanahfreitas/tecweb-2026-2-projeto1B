from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tags_input = request.POST.get('tags', '')

        note = Note.objects.create(title=title, content=content)

        tag_names = [t.strip() for t in tags_input.split(',') if t.strip()]
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            note.tags.add(tag)

        return redirect('index')

    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})

def delete(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')

def edit(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.save()

        tags_input = request.POST.get('tags')
        note.tags.clear()
        if tags_input:
            tag_names = [name.strip() for name in tags_input.split(',') if name.strip()]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                note.tags.add(tag)

        return redirect('index')
    else:
        return render(request, 'notes/edit.html', {'note': note})

def tags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': all_tags})

def tag_detail(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    notes = Note.objects.filter(tags=tag)
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': notes})
