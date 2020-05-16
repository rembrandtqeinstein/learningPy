import pdfplumber
pdf = pdfplumber.open('pythonlearn.pdf')
page = pdf.pages[3]
text = page.extract_text()
print(text)
pdf.close()