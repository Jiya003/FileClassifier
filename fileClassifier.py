import os
import shutil
from pathlib import Path
import time
#All the Files and Directory in The Download:
name=input("Enter Your Name:")
print("Hello!",name)
print("Welcome to the File Classifier Project by Divyanshi Maurya-12219959: :)")
print("Please Input File Path in correct Format :")
print("C://Users//Divyanshi//Downloads")
path = input()
time.sleep(3)
dir_list = os.listdir(path)
print("The number of Files and Directories in the Folder is:",len(dir_list))
print("The List of Files and directories in '", path, "' :")
print(*dir_list,sep="\n")

print()
print("-"*50)
print()
#Filtering only the files:

files = os.listdir(path)
files = [f for f in files if os.path.isfile(path+'/'+f)]
print("The no. of files in the Folder is:",len(files))
print("All the Files in the Folder is:")
print(*files, sep="\n")
print()
print("-"*50)
print()

#Filtering only pdf files:
pdffiles = [f for f in files if f.endswith(".pdf")]
if len(pdffiles)==0:
    print("The no. of files in the Folder is:", len(pdffiles))
    print("Hence,There is No pdf Files")
else:
    print("The no. of files in the Folder is:", len(pdffiles))
    print("All the pdf Files in The Folder:")
    print(*pdffiles, sep="\n")
print()
print("-"*50)
print()


#Filtering only text files:
textfiles = [f for f in files if f.endswith(".txt")]
if len(textfiles)==0:
    print("The no. of files in the Folder is:", len(textfiles))
    print("Hence,There is No text Files")
else:
    print("The no. of files in the Folder is:", len(textfiles))
    print("All the text Files in The Folder:")
    print(*textfiles, sep="\n")
print()
print("-"*50)
print()

#Filtering only jpeg files:
jpegfiles = [f for f in files if f.endswith(".jpeg")]
if len(jpegfiles)==0:
    print("The no. of files in the Folder is:", len(jpegfiles))
    print("Hence,There is No jpeg Files")
else:
    print("The no. of files in the Folder is:", len(jpegfiles))
    print("All the jpeg Files in The Folder")
    print(*jpegfiles, sep="\n")
print()
print("-"*50)
print()

#Filtering only jpg files:
jpgfiles = [f for f in files if f.endswith(".jpg")]
if len(jpgfiles)==0:
    print("The no. of files in the Folder is:", len(jpgfiles))
    print("Hence,There is No jpg format Files")
else:
    print("The no. of files in the Folder is:", len(jpgfiles))
    print("All the jpg Files in The Folder:")
    print(*jpgfiles, sep="\n")
print()
print("-"*50)
print()

#Filtering only png files:
pngfiles = [f for f in files if f.endswith(".png")]
print("The no. of files in the Folder is:",len(pngfiles))
if len(pngfiles)==0:
    print("There is No png format Files")
else:
    print("The no. of files in the Folder is:", len(pngfiles))
    print("All the png Files in The Folder:")
    print(*pngfiles, sep="\n")
print()
print("-"*50)
print()

#Filtering only exe files:
exefiles = [f for f in files if f.endswith(".exe")]
if len(exefiles)==0:
    print("The no. of files in the Folder is:", len(exefiles))
    print("Hence,There is No exe format Files")
else:
    print("The no. of files in the Folder is:", len(exefiles))
    print("All the exe Files in The Folder:")
    print(*exefiles, sep="\n")
print()
print("-"*50)
print()

#Filtering only xlsx files:
xlsxfiles = [f for f in files if f.endswith(".xlsx")]
if len(xlsxfiles)==0:
    print("The no. of files in the Folder is:", len(xlsxfiles))
    print("Hence,There is No Excel format Files")
else:
    print("The no. of files in the Folder is:", len(xlsxfiles))
    print("All the Excel Files in The Folder:")
    print(*xlsxfiles, sep="\n")
print()
print("-"*50)
print()

#Filtering only zip files:
zipfiles = [f for f in files if f.endswith(".zip")]
if len(zipfiles)==0:
    print("The no. of files in the Folder is:", len(zipfiles))
    print("There is No Zip format Files")
else:
    print("The no. of files in the Folder is:", len(zipfiles))
    print("All the Zip Files in The Folder")
    print(*zipfiles, sep="\n")
print()
print("-"*50)
print()
pdf = Path('pdf/')
pdf.mkdir(exist_ok=True)
txt = Path('txt/')
txt.mkdir(exist_ok=True)
png = Path('png/')
png.mkdir(exist_ok=True)
jpeg = Path('jpeg/')
jpeg.mkdir(exist_ok=True)
jpg = Path('jpg/')
jpg.mkdir(exist_ok=True)
xlsx= Path('xlsx/')
xlsx.mkdir(exist_ok=True)
exe = Path('exe/')
exe.mkdir(exist_ok=True)
zip= Path('zip/')
zip.mkdir(exist_ok=True)

source_folder = r"C://Users//Divyanshi//test//"

destination_folder = r"C://Users//Divyanshi//PycharmProjects//FileClassifier//txt//"
#Moving Text Files
for file_name in textfiles:
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
print()
print("-"*50)
print()

destination_folder1 = r"C://Users//Divyanshi//PycharmProjects//FileClassifier//pdf//"
#Moving pdf files
for file_name in pdffiles:
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder1 + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
print()
print("-"*50)
print()
destination_folder2 = r"C://Users//Divyanshi//PycharmProjects//FileClassifier//exe//"
#Moving Exetension Files
for file_name in exefiles:
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder2 + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
print()
print("-"*50)
print()
destination_folder3 = r"C://Users//Divyanshi//PycharmProjects//FileClassifier//png//"
#Moving png Files
for file_name in pngfiles:
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder3 + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
print()
print("-"*50)
print()
destination_folder4 = r"C://Users//Divyanshi//PycharmProjects//FileClassifier//jpg//"
#Moving jpg Files
for file_name in jpgfiles:
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder4 + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
print()
print("-"*50)
print()
destination_folder5 = r"C://Users//Divyanshi//PycharmProjects//FileClassifier//zip//"
#Moving Zip Files
for file_name in zipfiles:
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder5 + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
print()
print("-"*50)
print()
destination_folder6 = r"C://Users//Divyanshi//PycharmProjects//FileClassifier//xlsx//"
#Moving Excel Files:
for file_name in xlsxfiles:
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder6 + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
print()
print("-"*50)
print()
destination_folder7 = r"C://Users//Divyanshi//PycharmProjects//FileClassifier//jpeg//"
#Moving Jpeg Files
for file_name in jpegfiles:
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder7 + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
print()
print("-"*50)
print()

#Text File to Store all the data:
file=open("History.txt",'w+r')
file.write("Hello!",name,"\n")
file.write("Welcome to the File Classifier Project by Divyanshi Maurya-12219959: :)")
file.write("The number of Files and Directories in the Folder is:",len(dir_list))
file.write("The no. of files in the Folder is:",len(files))
file.write("The no. of Directory in the Folder is:",(len(dir_list)-len(files)))
file.write("The no. of files in the pdf format is:", len(pdffiles))
file.write("The no. of files in the png format is:", len(pngfiles))
file.write("The no. of files in the jpg format is:", len(jpgfiles))
file.write("The no. of files in the jpeg is:", len(jpegfiles))
file.write("The no. of files in the zip format is:", len(zipfiles))
file.write("The no. of files in the exe format is:", len(exefiles))
file.write("The no. of files in the excel format is:", len(xlsxfiles))
file.close()

