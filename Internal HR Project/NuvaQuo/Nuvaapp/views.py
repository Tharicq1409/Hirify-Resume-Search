from django.shortcuts import render
from django.urls import reverse
#from .utils import search_pdfs  #to import code from utils.py
import os
import pdfplumber
from django.http import HttpResponse, FileResponse
from urllib.parse import quote
# Create your views here.
def welcome(request):
    return render(request, 'app1/Main.html')

#old code to search for 1 term
'''
def search_result(request):
    results = None
    search_term =''
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        if search_term:
            # Modify the results list to include tuples of (file_path, file_name)
            results = [(os.path.join(root, file).replace('/', '\\'), file) for root, _, files in os.walk('C:/Users/3iintr00203/Desktop/resumes') for file in files if file.endswith('.pdf') and search_term.lower() in pdfplumber.open(os.path.join(root, file)).pages[0].extract_text().lower()]
            #results = search_pdfs('C:/Users/3iintr00203/Desktop/resumes/perfect resumes', search_term)
    return render(request, 'app1/sample.html', {'results': results,'search_term':search_term})'''

#updated code to search 3 terms
def search_result(request):
    results = []
    search_term1 = ''
    search_term2 = ''
    search_term3 = ''
    if request.method == 'POST':
        search_term1 = request.POST.get('search_term1')
        search_term2 = request.POST.get('search_term2')
        search_term3 = request.POST.get('search_term3')
        if search_term1:
            root_dir = 'C:/Users/3iintr00203/Desktop/resumes'
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    if file.endswith('.pdf'):
                        with pdfplumber.open(os.path.join(root, file)) as pdf:
                            found_search_terms = [False, False, False]
                            for page in pdf.pages:
                                text = page.extract_text()
                                if search_term1.lower() in text.lower():
                                    found_search_terms[0] = True
                                if search_term2 and search_term2.lower() in text.lower():
                                    found_search_terms[1] = True
                                if search_term3 and search_term3.lower() in text.lower():
                                    found_search_terms[2] = True
                            if found_search_terms[0] and (not search_term2 or found_search_terms[1]) and (not search_term3 or found_search_terms[2]):
                                results.append((os.path.join(root, file).replace('/', '\\'), file))
                                print(f"Found '{search_term1}', '{search_term2}', and '{search_term3}' in {file}")
                            else:
                                print(f"One or more search terms not found in {file}")
    return render(request, 'app1/results.html', {'results': results, 'search_term1': search_term1, 'search_term2': search_term2, 'search_term3': search_term3})
