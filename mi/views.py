from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rohit(request):
    return render(request,'rohit.html')

def sky(request):
    return HttpResponse("<h1><morquee>This is sky</morquee></h1>")
