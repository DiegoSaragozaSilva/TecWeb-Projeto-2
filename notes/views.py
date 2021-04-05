from django.shortcuts import render
from .models import Note, Tag


def index(request):
    all_notes = Note.objects.all()

    if request.method == 'POST':
        
        request_type = request.POST.get('type')

        if(request_type == 'create'):
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            tag = request.POST.get('tag')
            new_note = Note(title = title, content = content, tag = tag)
            new_note.save()
            
            _add_id_to_tag(new_note.id, tag)

        elif(request_type == 'edit'):

            for note in all_notes:
                if note.title ==  request.POST.get('org_title') and note.content == request.POST.get('org_content') and note.tag == request.POST.get('org_tag'):
                    note_edit = Note.objects.get(pk = note.id)
                    note_edit.title = request.POST.get('titulo')
                    note_edit.content = request.POST.get('detalhes')
                    note_edit.tag = request.POST.get('tag')
                    note_edit.save()

                    if request.POST.get('tag') != request.POST.get('org_tag'):
                        _edit_id_tag(note_edit.id, request.POST.get('org_tag'), request.POST.get('tag'))

                    break
        elif(request_type == 'delete'):
            print("AAA")
            for note in all_notes:
                print(note.title, request.POST.get('org_title'))
                print(note.content, request.POST.get('org_content'))
                print(note.tag, request.POST.get('org_tag'))

                if note.title == request.POST.get('org_title') and note.content == request.POST.get('org_content') and note.tag == request.POST.get('org_tag'):
                    print("AAA")
                    note_delete = Note.objects.get(pk = note.id)
                    _delete_id_from_tag(note_delete.id, note_delete.tag)
                    note_delete.delete()
                    break
        
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def tags(request):
    all_tags = Tag.objects.all()
    if(request.method == 'POST'):
        tag_name = request.POST.get('tag_name')
        for tag in all_tags:
            if tag.name == tag_name:
                notes_ids = tag.notes_ids
                print(notes_ids)
                notes = [Note.objects.get(pk = int(_id)) for _id in notes_ids]
                
                return render(request, 'notes/tag_one.html', {'selected_notes': notes})

    return render(request, 'notes/tags.html', {'tags': all_tags})

def _add_id_to_tag(note_id, tag_name):
    all_tags = Tag.objects.all()

    for tag in all_tags:
        if tag.name == tag_name:
            tag.notes_ids.append(note_id)
            tag.save()
            return
    
    new_tag = Tag(name = tag_name, notes_ids = [note_id])
    new_tag.save()

def _edit_id_tag(note_id, old_tag, new_tag):
    all_tags = Tag.objects.all()

    tag_1, tag_2 = None, None

    for tag in all_tags:
        if old_tag == tag.name:
            tag_1 = tag
        elif new_tag == tag.name:
            tag_2 = tag

    if tag_2 == None:
        tag_2 = Tag(name = new_tag, notes_ids = [])
        tag_2.save()
    
    tag_1.notes_ids.remove(note_id)
    tag_2.notes_ids.append(note_id)
    tag_1.save()
    tag_2.save()

def _delete_id_from_tag(note_id, note_tag):

    all_tags = Tag.objects.all()

    for tag in all_tags:
        if note_tag == tag.name:
            tag.notes_ids.remove(note_id)
            tag.save()
            return
