from django.shortcuts import render, HttpResponse

# Create your views here.
def foo_home(request):
    return render(request, 'home.html')

