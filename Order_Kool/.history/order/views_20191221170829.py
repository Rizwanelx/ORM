from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def detail(request):
    return HttpResponse("You're looking at question")


def loginView(request, myid):
    return render(request, 'shop/prodView.html')