from django.shortcuts import render
from .forms import NameForm

# Create your views here.
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            return render(request, 'form.html', {"form": NameForm(), "username":username})
    else:
     return render(request, 'form.html', {"form":NameForm()})
