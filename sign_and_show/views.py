from django.shortcuts import render
from django.http import HttpResponse

def getDocument(request):
    return render(request, 'index.html')