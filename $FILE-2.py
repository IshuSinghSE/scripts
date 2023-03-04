import os, shutil, time
import glob, json
from shutil import move


### Download Path ####
X = "D:\\Downloads\\"

DEST="D:\\Downloaded\\"
SOURCE=glob.glob( X + "*")

Y = DEST + "Directoy\\"


#### File Extension ####
dict={
    'Documents'       :['txt','csv'],
    'Documents\\PDF'  :['pdf'],
    'Documents\\Docx' :['docx','doc','xls','xlsx','ppt','pptx'],
    'Image'     :['png','jpg','jpeg','gif','webp','raw','svg'],
    'Movies'    :['webm','mp4','mpg','mkv','mpeg','wmv','mov'],
    'Music'     :['mp3','wav','weba','m4r','ogg','vlc','wax','wma','opus','aud','m4a','flac','acc'],
    'Program'   :['bat','bin','cmd','cpl','lnk','msc','msp','shs','ws'],
    'Setup'     :['exe','msi'],
    'Zips'      :['zip','rar','tar','7z','gz','sitx','xapk','tarxz','war','zpi','xar','zz','zap'],
    'Apps'      :['apk','pkg'],
    'Python'    :['py','pyc'],
    'Others'    :['lst','json'],
    'Html'      :['html','mhtml',],
    'Msixbundle':['msixbundle',],
    }

##### Extension #####
#NOTE : Enter in same oreder as in dict
zips = ['Documents','Documents\\PDF','Documents\\Docx','Image','Movies','Music','Program','Setup','Zips','Apps','Python','Others','Html','Msixbundle']

#folder locations
folders = [] # "D:/destination/folder-name/ of all folders

#folders =[DocumentsDstation,ProgramDstation,MoviesDstation,MusicDstation,ImageDstation,SetupDstation,ZipsDstation,AppsDstation]

# Get folder paths
def Location(zips): #✔✔✔
    global DEST
    if not os.path.exists(DEST):
        os.mkdir(DEST)
               
    for folder in zips:
        name = os.path.join(DEST , (folder + '\\'))
        folders.append(name)

        
#for moving files to destination folders        
def sorter_file(FileExts, folder): #✔✔✔
    global SOURCE
    for file in SOURCE:
        if file != str(DEST) + '$FILE-2.py':
            ext = os.path.splitext(file)[1][1:]
            
            
             #current folder file extensions
            if ext in FileExts:
                if not (os._exists(file)):
                    if(os.path.exists(folder)):
                        move(file,folder)#, copy_function = shutil.copy2)
                        print('succesful.')
                    else:
                        os.mkdir(folder)
                        move(file,folder)#, copy_function = shutil.copy2)
                        print('succesful!')
                else:
                    print('exits')#os.remove(file))
                print("Files sorted!")    
  
#for moving directories to destination folders   
def sorter_folder(x, y): #✔✔✔   
    
    for dir in os.listdir(x):
        src = x + dir
        dst = y + dir
       
        if os.path.isdir(src):
            if(os.path.exists(y)):
                    move(src,dst, copy_function = shutil.copytree)
                    print("moved :", dir)
                    src, dst = '', ''
                    
            else:
                os.mkdir(y)
                print('Directoy created')
                move(src,dst, copy_function = shutil.copytree)
                print("moved :", dir)
                src, dst = '', ''      
    
    print("Directoy sorted!")
#### func-call ####

#if __name__ == '__main__':

Location(zips)
Extension = dict.values()

for Extensions, Folder in zip(Extension,folders):
        sorter_file(Extensions, Folder)
         
sorter_folder(X,Y)