from django.forms import ModelForm
from .models import document

class DocumentForm(ModelForm):
    class Meta:
        model = document
        fields = ['docfile']