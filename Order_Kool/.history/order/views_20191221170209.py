from django.shortcuts import render

# Create your views here.

def Home(request):
    
    return render(request, 'order/index.html')
