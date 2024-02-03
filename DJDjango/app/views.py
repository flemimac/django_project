from django.shortcuts import render
from app.models import friends

def index(request):
    friends.objects.get(id = 2).delete()

    all = friends.objects.all()
    print(all)
    
    return render(request, "index.html")

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')