from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many pdfs u want to merge : "))

for i in range(0, n):
    name = input("Enter pdf name with extensions : ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("Merged_pdf.pdf")
merger.close()