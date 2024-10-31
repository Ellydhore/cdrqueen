from django.shortcuts import render, HttpResponse

# Create your views here.
def to_recieve(request):
    return render(request, 'to_recieve.html')
