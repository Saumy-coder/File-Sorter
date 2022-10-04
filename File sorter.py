import os
import shutil


print("Added a functionality of sub folders \n Note: There should not be any folders withing the subfolder ")
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
            dest1 = dest +'/'+ext[1:] +'/'+name + ext
            if(os.path.exists(dest+'/'+ext[1:])==True):
                paste = shutil.copy(source1,dest1)
            else:
                os.makedirs(dest+'/'+ext[1:])
                paste = shutil.copy(source1,dest1)
        elif(ext == ''):
            subexten = []
            subpath = source+'/'+ name
            subfiles = os.listdir(subpath)
            for p in subfiles:
                subname,subext = os.path.splitext(p)
                for a in range(0,len(subfiles)):
                    if(subext not in subexten):
                        subexten.append(subext)
            
                for b in range(0,len(subexten)):
                    if(subext==subexten[b]):
                        subsource1 = subpath + '/' + subname + subext
                        subdest1 = dest +'/'+ subext[1:] +'/'+name + '/' +subname + subext
                        if(os.path.exists(dest +'/'+ subext[1:] +'/'+name)==True):
                            paste = shutil.copy(subsource1,subdest1)
                        else:
                            os.makedirs(dest +'/'+ subext[1:] +'/'+name)
                            paste = shutil.copy(subsource1,subdest1)
