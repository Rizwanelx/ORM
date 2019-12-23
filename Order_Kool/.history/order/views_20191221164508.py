from django.shortcuts import render

# Create your views here.

def LoginHome(request):
    
    return render(request, 'order/index.html')
