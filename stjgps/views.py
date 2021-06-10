from django.shortcuts import render,HttpResponse
from . models import LegalDoc

# Create your views here.
def home(request):
    return render(request,'index.html')

def documentation(request):
    return render(request,'documents.html',{"legal_docs":LegalDoc.objects.all()})
