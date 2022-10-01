import os
import shutil


print("There should not be any folder withing the initial folder ")
sourced = input("Enter main folder:")    
source = sourced.replace("\\",'/')
destd = input("Enter the folder to create the new folders: ")
dest = destd.replace("\\",'/')

files = os.listdir(source)
exten = []
for x in files:
    name,ext = os.path.splitext(x)
    for i in range(0,len(files)):
        if(ext not in exten):
            exten.append(ext)
    
    for y in range(0,len(exten)):
        if (ext == exten[y]):
            source1 = source+'/'+name + ext
            dest1 = dest +'/'+ext +'/'+name + ext
            if(os.path.exists(dest+'/'+ext)==True):
                paste = shutil.copy(source1,dest1)
            else:
                os.makedirs(dest+'/'+ext)
                paste = shutil.copy(source1,dest1)
        