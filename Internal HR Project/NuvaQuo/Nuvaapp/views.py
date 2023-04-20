from django.shortcuts import render
from django.urls import reverse
from .utils import search_pdfs
import os
import pdfplumber
from django.http import HttpResponse, FileResponse
from urllib.parse import quote
# Create your views here.
def welcome(request):
    return render(request, 'app1/Main.html')

def search_result(request):
    results = None
    search_term =''
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        if search_term:
            # Modify the results list to include tuples of (file_path, file_name)
            results = [(os.path.join(root, file).replace('/', '\\'), file) for root, _, files in os.walk('C:/Users/3iintr00203/Desktop/resumes/perfect resumes') for file in files if file.endswith('.pdf') and search_term.lower() in pdfplumber.open(os.path.join(root, file)).pages[0].extract_text().lower()]
            #results = search_pdfs('C:/Users/3iintr00203/Desktop/resumes/perfect resumes', search_term)
    return render(request, 'app1/sample.html', {'results': results,'search_term':search_term})