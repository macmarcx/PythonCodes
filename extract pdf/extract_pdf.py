import pdfplumber
import pandas as pd
import os

# Define the directory where PDF files are stored
pdf_dir = "path/to/your/pdf_files"
extracted_data = []

# Function to extract the desired value from each PDF
def extract_value(pdf_path, keyword):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if keyword in text:
                # Find the specific value after the keyword
                value = text.split(keyword)[1].split()[0]  # Extracts the first value after the keyword
                return value
    return None

# Keyword you want to search for in the PDFs
keyword = "YourDesiredValue"

# Loop through all PDF files in the specified directory
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        value = extract_value(pdf_path, keyword)
        if value:
            extracted_data.append({"File": filename, "Value": value})

# Convert the list of data into a pandas DataFrame and export to Excel
df = pd.DataFrame(extracted_data)
df.to_excel("extraction_result.xlsx", index=False)
