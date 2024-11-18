from PIL import Image
import cv2
import encodings

import encodings.ascii
import CryptData

def decimalToBinary(dec):
    pass

def dz(num):
    res=[]
    for i in range(1,num):
        if num%i==0:res.append(i)
    return res

def getSizeXY(num):
    height=dz(num)
    height=height[int((len(height)-1)/2)]
    width=int(num/height)
    return (width,height)

def roundToUp(v):
    if (v-int(v))!=0: return int(v)+1
    return int(v)

def __readFileAsByteArray(path):
    f=open(path,"rb")
    data=f.read()
    f.close()
    data=CryptData.CryptByteArray(data)
    res=[]
    for b in data:
        res.append(int(b))
    return res

def __saveByteArrayToImage(bytes,name,format):
    width,height=getSizeXY(roundToUp((len(bytes)/3)))
    im=Image.new("RGB",(width,height))
    for y in range(0,height):
        for x in range(0,width):
            if(len(bytes)<=0):
                im.putpixel((x,y),(0,0,0))
                continue
            r,g,b=0,0,0
            r=bytes[0]
            bytes.pop(0)
            if(len(bytes)>0):
                g=bytes[0]
                bytes.pop(0)
            if(len(bytes)>0):
                b=bytes[0]
                bytes.pop(0)
            im.putpixel((x,y),(r,g,b))
    im.save(f"./{name}.{format}",format)

def Convert(path,save_name,format):
    __saveByteArrayToImage(__readFileAsByteArray(path),save_name,format)


def Read(path,save_name,format):
    f=cv2.imread(path)
    height,width,k=f.shape
    data=[]
    for y in range(0,height):
        for x in range(0,width):
            color=f[y][x]
            data.append(color[2])
            data.append(color[1])
            data.append(color[0])
    #Saving Readed Data
    f=open(f"{save_name}.{format}","wb")
    for b in data:
        if(b==0):continue
        f.write(b)
    f.close()
    #Decryting File
    f=open(f"{save_name}.{format}","rb")
    data=CryptData.DeCryptByteArray(f.read())
    f.close()
    #Saving Decrypted File
    f=open(f"{save_name}.{format}","w")
    f.write(data)
    f.close()

def SaveString(name,format,data):
    d=bytearray()
    d.extend(map(ord, data))
    d=CryptData.CryptByteArray(bytes(d))
    data=[]
    data.extend(map(int,d))
    __saveByteArrayToImage(data,name,format)


import json
import random

my_test_array=[324,234,222,3534,345234,234]

for i in range(0,1500):
    my_test_array.append(random.randrange(0,100))

SaveString("resB","png",str(json.dumps(my_test_array)))

#Convert("./test.dat","res","png")
Read("./resB.png","readed","txt")