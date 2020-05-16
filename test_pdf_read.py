import pdfplumber

# Routing the comptuer to a PDF. The PDF Name needs to be without spaces
#url = 'C:/Users/Hernan Herrera Hall/Desktop/Libros/Negocios y Producto/Email_optimization___best_practices_2018.pdf'
#pdf = pdfplumber.open(url)

pdf = pdfplumber.open('quixote.pdf')

#page = pdf.pages[3]
#text = page.extract_text()

# Letter Frequency Counter Part
hist = dict()
text = ''
#count = 0
for page in pdf.pages:
    text = text + page.extract_text()
    #count = count +1
    #print(text)

#print(text)
#print(len(pdf.pages))

for w in text:
    w = w.lower()
    if w.isalpha():
        hist[w] = hist.get(w, 0) + 1
    #print(w)

print("Letter Frequency for the PDF: ")
ord = sorted([(v,k) for k,v in hist.items()], reverse=True)
for v,k in ord:
    print(k,v)

# Word Count Part
whist = dict()
for pages in pdf.pages:
    text = pages.extract_text()
    text = text.split()
    for t in text:
        t = t.lower()
        if t.isalpha():
            whist[t] = whist.get(t, 0) + 1

print()
print("Word Frequency for the PDF: ")
w_ord = sorted([(v,k) for k,v in whist.items()], reverse=True)
for v,k in w_ord:
    if v > 10:
        print(k,v)

#print(whist)

pdf.close()

