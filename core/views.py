from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request , 'index.html')    

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
    else:
        return render(request, 'signup.html')
    
