import os
import pdfplumber
import os.path


def search_pdfs(root_dir, search_term):
    results = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.pdf'):
                # Initialize flag variable
                found_search_term = False
                with pdfplumber.open(os.path.join(root, file)) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()
                        if search_term.lower() in text.lower():
                            # Set flag to True if search term is found
                            found_search_term = True
                # Append file path to results list if search term is found for the first time in the file
                if found_search_term:
                    file_name = os.path.basename(file)
                    if file_name not in results: 
                        print(f"Found '{search_term}' in {file_name}")
                        results.append(file_name)
    # Return list of matching file paths with each file path printed only once
    return list(set(results))                
'''
                    file_path = os.path.join(root, file)
                    print(f"Found '{search_term}' in {file_path}")
                    results.append(f"'{search_term}' found in '{file_path}'")'''
                    #results.append(os.path.join(root, file))
    

#url = quote(os.path.relpath(os.path.join(root, file), root_dir).replace('/', '\\'))
#results.append(url)