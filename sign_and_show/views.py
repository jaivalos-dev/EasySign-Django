from django.shortcuts import render
from django.http import HttpResponse
from .forms import DocumentForm

def getDocument(request):
    if request.method == 'GET':
        return render(request, 'index.html', {
            'form': DocumentForm
        })
    else: 
        try:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse('File uploaded successfully')
            else:
                return HttpResponse('Form is not valid')
        except:
            return render(request, 'index.html', {
                'form': DocumentForm,
                'error': 'An error occurred. Please try again.'
            })
            
            
def showDocument(request):
    return render(request, 'show.html')