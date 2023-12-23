# Write a program to manipulate pdf files using pyPDF. 
# Your programs should be able to merge multiple pdf files into 
# a single pdf. You are welcome to add more functionalities
# pypdf is a free and open-source pure-python PDF library 
# capable of splitting, merging, cropping, and transforming 
# the pages of PDF files. It can also add custom data, viewing 
# options, and passwords to PDF files. pypdf can retrieve text 
# and metadata from PDFs as well.

from PyPDF2 import PdfWriter
import os

class PdfMerger:
    
    def __init__(self):
        self.merger = PdfWriter()
        self.pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]
                
    def merge(self, output_filename = "merged-pdf.pdf"):
        self.output = output_filename
        for pdf in self.pdf_files:
            with open(pdf, 'rb') as file:
                self.merger.append(file)

        with open(self.output, 'wb') as output_file:
            self.merger.write(output_file)
        self.merger.close()

object = PdfMerger()
object.merge()
    