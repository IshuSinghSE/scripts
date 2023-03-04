import os
import glob
import shutil
from shutil import move, copy2
from os import path


filename=glob.glob("D:/Downloads/*")

Documents=['pdf','docx','doc','txt','xls','xlsx','ods','ppt','pptx','pyc']
Program =['bat','bin','cmd','cpl','lnk','msc','msp','shs','ws','html','xml','mhtml']
Movies=['webm','mp4','MP4','mpg','mp2','mp4','mpeg','wmv','mov']
Music=['mp3','wav','weba','m4r','ogg','vlc','wax','wma','opus','aud','m4a','flac','acc']
Image=['png','jpg','jpeg','JPG','JPEG','PNG','gif','webp','raw','svg']
Setup=['exe','msi']
Zips=['zip','rar','tar','7z','gz','sitx','xapk','tar.xz','war','zpi','xar','zz','zap','xz','tgz']
Apps=['apk','pkg']
Icons =['ico','bmp']
Extension = ['vsix']
Json = ['json']


Loc = "D:/Downloaded/"
# print(filename,Loc)

DocumentsLocation=Loc + 'Documents'
ProgramLocation = Loc + 'Program'
MoviesLocation=Loc + 'Movies'
MusicLocation = Loc + 'Music'
ImageLocation = Loc + 'Image'
SetupLocation=Loc + 'Setup'
ZipsLocation=Loc + 'Zips'
AppsLocation=Loc + 'Apps'
IconLocation=Loc + 'Icons'
ExtensionLocation= Loc + 'Extension/VS-CODE'
JsonLocation=Loc + 'Json'

zips = [Documents,Program,Movies,Music,Image,Setup,Zips,Apps,Icons,Extension, Json]
folder =[DocumentsLocation,ProgramLocation,MoviesLocation,MusicLocation,ImageLocation,SetupLocation,ZipsLocation,AppsLocation,IconLocation,ExtensionLocation, JsonLocation]


def sorter(zippy, folder):
    global filename
    for file in filename:
        ext = path.splitext(file)[1][1:]
        

        if ext in zippy:
            if(path.exists(folder)):
               
                move(file,folder)
                print('succesful.')
            else:
                os.mkdir(folder)
                move(file,folder)
                print('succesful!')
                
                

for zippy, foldy in zip(zips,folder):
    #sorter(zippy,foldy)
    print(zippy,foldy)
print('files sorted!')
    