#Researching from
#https://pythonhosted.org/PyPDF2/PdfFileReader.html

import PyPDF2

filen=(input("Enter the pdf file you would like to convert: "))
filen=str(filen+'.pdf')


a=PyPDF2.PdfFileReader(filen)
#print(a.documentInfo)

pages=a.getNumPages()

Str = ""

for i in range(0, pages):
    Str += a.getPage(i).extractText()

with open("text.txt", "w", encoding='utf-8') as file:
    file.write(Str)