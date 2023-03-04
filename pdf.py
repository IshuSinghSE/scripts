from PyPDF2 import PdfReader, PdfWriter, Transformation
from PyPDF4 import PdfFileMerger 
from PyPDF2.generic import RectangleObject
import os 

#from (1654, 2339) , to (595,841)
PDFS = []

def pages(path):
    global PDFS
    for pdf in os.listdir(path):
        if pdf.endswith(".pdf"):
            PDFS.append(pdf)
                        
def size(img, index):
    for path in img:
        with open(path, mode="rb") as f:
            input_pdf = PdfReader(f)
            media_box = input_pdf.pages[index-1].mediabox
            page = input_pdf.pages[index-1]
            #scale page to given values
            page.scale_to(595.0 ,841.0)
            min_pt = media_box.lower_left
            max_pt = media_box.upper_right
            pdf_w = max_pt[0] - min_pt[0]
            pdf_h = max_pt[1] - min_pt[1]
            
            #resizing and adding pages
            pdf_writer = PdfWriter()
            pdf_writer.add_page(page)
            
            #Creating resized pages
            with open(path,"wb") as output_file:
              pdf_writer.write(output_file) 
              
    #page size after resizing 
    print(path,"w - ",pdf_w, "h - ", pdf_h)
        
def merge_pdfs(input_files: list, page_range: tuple, output_file: str, bookmark: bool = True):
    
    merger = PdfFileMerger(strict=False)
    for input_file in input_files:
        bookmark_name = os.path.splitext(os.path.basename(input_file))[0] 
        # pages To control which pages are appended from a particular file.
        merger.append(fileobj=open(input_file, 'rb'), pages=page_range, import_bookmarks=False, bookmark=bookmark_name)
    # Insert the pdf at specific page
    merger.write(fileobj=open(output_file, 'wb'))
    merger.close()
        
#with open(img[0], mode="rb") as f:
#            input_pdf = PdfReader(f)
#            media_box = input_pdf.pages[0].mediabox
#            print(media_box)
#merge_pdfs(img,(0,1),"merge.pdf")   