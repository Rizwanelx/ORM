from django.shortcuts import render

# Create your views here.

def LoginHome(request):
    
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'order/')
