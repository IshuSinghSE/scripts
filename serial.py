from PyPDF2 import PdfReader, PdfWriter, Transformation 
from PyPDF2.generic import RectangleObject
from PyPDF4 import PdfFileMerger
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
import os, time
#from (1654, 2339) , to (595,841)

#page storer
def pages(path):#✅
    global PDFS, DIR
    for pdf in os.listdir(path):
        if pdf.endswith(".pdf"):
            PDFS.append(( DIR + pdf))  
    PDFS.sort(key=os.path.getmtime)
    print(" * pdfs stored in list !")
    return PDFS
                    
#directory   creator     
def folder(pathname): #✅
    if not os.path.isdir(pathname):
            os.makedirs(pathname)  
            print(" * Created ! ", pathname)

#resizer                        
def size(images):#✅
    for img in images:
        with open(img, mode="rb") as f:
            input_pdf = PdfReader(f)
            media_box = input_pdf.pages[0].mediabox
            page = input_pdf.pages[0]
            #scale page to given values
            width =  595.0
            height = 842.0
            page.scale_to(width, height)#(595.0 ,841.0)
            op = Transformation().scale(sx=0.99, sy=0.96)
            page.add_transformation(op)
            min_pt = media_box.lower_left
            max_pt = media_box.upper_right
            pdf_w = max_pt[0] - min_pt[0]
            pdf_h = max_pt[1] - min_pt[1]
            
            #resizing and adding pages
            pdf_writer = PdfWriter()
            pdf_writer.add_page(page)
            
            #Creating resized pages
            with open(img,"wb") as output_file:
              pdf_writer.write(output_file) 
              
    #page size after resizing 
    print(" * All image resized to ", width, height, " !")

#Takes input: []  & (start, end) & str        
def merge_pdfs(input_files: list, page_range: tuple, output_file: str):#✅
    global MERGER ,PDFS
    folder(MERGER)
    time.sleep(.1)
    merger = PdfFileMerger(strict=False)
    for input_file in tqdm(input_files, desc=" * Merging <"):
        # pages To control which pages are appended from a particular file
        merger.append(fileobj=open(input_file, 'rb'), pages=page_range)
        
    # Insert the pdf at specific page
    merger.write(fileobj=open(output_file, 'wb'))
    merger.close()
    print(" * ", MERGER.split('/')[0], "Pdfs merged !")
    time.sleep(.3)

#numbering pages                                
def serial(x):   #✅
    global  DIR, FONT
    #open image file
    img = Image.open(r'billbook.jpg')
    filename= DIR  + str(x) + ".pdf"
 
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
 
    # Custom font style and font size
    leftFont = ImageFont.truetype(FONT, 60)
    rightFont = ImageFont.truetype(FONT, 40)   
    
    # Add Text to an image
    I1.text((190, 345), x, font=leftFont, fill =(0, 0, 0))
    I1.text((1550, 305), x, font=rightFont, fill =(0, 0, 0))
   
    #Rotate image
    rotate_img =  img.transpose(Image.ROTATE_270)
    
    #covert to pdf format
    img.convert('RGB')
     # Save rotated & edited image
    rotate_img.save(filename)

def loop(start, end): #✅
        global DIR
        #creating directory
        folder(DIR)
        #printing page no on each page
        for x in tqdm(range(start,end+1),desc=" * Printing <", colour="white"):
              if x<10:
                  x = "00" + str(x)
                  serial(x)
              elif x<100:
                 x = "0" + str(x)
                 serial(x)
              else:    
                x = str(x)
                serial(x)
        print(" * Serialize & saved to '", DIR[:-1], "' !")
        
   
            
START =   int(input("  Enter  starting value: e.g 1 &  > "))  
END =    int(input("  Enter  ending value: e.g 10 &   > "))    

DIR  = str(START) + "-" + str(END) + "/"
MERGER = DIR + "pdf" + "/" 
FONT = 'gabriele-bad.ttf'

PDFS = []
TUPLE = (0,1)

merged_file = MERGER + DIR[:-1] +  ".pdf"

loop(START, END)                
size(pages(DIR))
merge_pdfs(PDFS,(0,1), merged_file)
                         
# output
print( " </3 Book pages  printed Successfully!")