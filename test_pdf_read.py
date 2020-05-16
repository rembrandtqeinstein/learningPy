import pdfplumber
pdf = pdfplumber.open('pythonlearn.pdf')
page = pdf.pages[3]
text = page.extract_text()
#count = 0

for page in pdf.pages:
    text = text + page.extract_text()
    #count = count +1
    #print(text)

hist = dict()
#print(text)
#print(len(pdf.pages))

for w in text:
    w = w.lower()
    if w.isalpha():
        hist[w] = hist.get(w, 0) + 1
    #print(w)
ord = sorted([(v,k) for k,v in hist.items()], reverse=True)
for v,k in ord:
    print(k,v)

pdf.close()

