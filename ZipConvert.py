import CryptData
from PIL import Image
import cv2

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

def moveIfPossible(array,v):
    if(len(array)>0):
        v=array[0]
        array.pop(0)
        return v
    return 0

def ByteArrayToArray(a):
    res=[]
    for e in a: res.append(int(e))
    return res

def Save(path,name):
    f=open(path,"rb")
    data=f.read()
    f.close()
    data=CryptData.CryptByteArray(data)
    data=ByteArrayToArray(data)
    width,height=getSizeXY(roundToUp((len(data)/3)))
    im=Image.new("RGB",(width,height))
    for y in range(0,height):
        for x in range(0,width):
            if len(data)<=0: continue
            r,g,b=0,0,0
            r=moveIfPossible(data,r)
            g=moveIfPossible(data,g)
            b=moveIfPossible(data,b)
            im.putpixel((x,y),(r,g,b))
    im.save(f"./{name}.png","png")

def Read(path,name,format):
    image=cv2.imread(path)
    height,width,k=image.shape
    data=""
    for y in range(0,height):
        for x in range(0,width):
            data+=chr(image[y][x][2])
            data+=chr(image[y][x][1])
            data+=chr(image[y][x][0])
    data=CryptData.fernet.decrypt(data)
    f=open(f"./{name}.{format}","wb")
    f.write(data)
    f.close()

#Save("./input.7z","result","jpeg")
Read("./result.jpeg","newInput","7z")