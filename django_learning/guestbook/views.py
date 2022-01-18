from django.shortcuts import render
from .forms import GuestbookForm
from .models import Message
from datetime import datetime
# Create your views here.

def get_guestbook(request):
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            newMessage = Message(pseudo=form.cleaned_data["pseudo"], body=form.cleaned_data["body"], pub_date=datetime.now())
            newMessage.save()
    return render(request, 'parts/guestbook.html',{"form":GuestbookForm(), "message_list":Message.objects.all()} ) 
