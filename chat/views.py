from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from .forms import MessageForm, RoomForm

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})


@login_required
def room_chat(request, room_id):
    room = Room.objects.get(id=room_id)
    messages = Message.objects.filter(room=room)
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.room = room
            message.save()
            return redirect('room_chat', room_id=room_id)
    return render(request, 'room_chat.html', {'room': room, 'messages': messages, 'form': form})

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def create_room(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Только суперпользователь может создать комнату.")
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            return redirect('room_chat', room_id=room.id)
    else:
        form = RoomForm()
    return render(request, 'create_room.html', {'form': form})
