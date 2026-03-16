from PyPDF2 import PdfMerger
import os
merger = PdfMerger()
print(os.listdir())
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged2.pdf")
merger.close()
print("PDFs merged successfully into 'merged2.pdf'")

