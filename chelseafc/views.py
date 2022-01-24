from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def samplefunction(request):
    return HttpResponse("hello")
def londonfun(request):
    return render(request,'akhil.html')
    