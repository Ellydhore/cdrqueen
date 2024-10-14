from django.shortcuts import render, HttpResponse

# Create your views here.
def foo_admin_dash(request):
    return render(request, 'dashboard.html')
