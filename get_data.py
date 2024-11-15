import cv2

def isEqual(a,b):
    if (a[0]==b[0])and(a[1]==b[1])and(a[2]==b[2]):return True
    return False

class Reader():
    path=""
    actual_bit=0
    width,height=0,0
    max_bits=0
    def __init__(self,path):
        self.path=path
        self.image=cv2.imread(path)
        self.width,self.height,k=self.image.shape
        #print(f"size {self.width}:{self.height}")
        self.max_bits=self.width*self.height
        #print(f"max bits {self.max_bits}")
    def read_next(self):
        x=int(self.actual_bit/self.width)
        y=int(self.actual_bit%self.width)
        color=self.image[x, y]
        res=None
        if(isEqual(color,[255,255,255])):
            res=1
        elif(isEqual(color,[0,0,0])):
            res=0
        self.actual_bit+=1
        if self.actual_bit>=self.max_bits: self.actual_bit=0
        return res

def read_file_data(name):
    f=open("data.txt","w")
    r=Reader(f"./result/{name}.png")
    bit_map=[]
    do_a=r.read_next()
    while do_a!=None:
        bit_map.append(do_a)
        do_a=r.read_next()
    bytes=[]
    for x in range(0,len(bit_map),8):
        bytes.append(bit_map[x:x+8])
    for b in bytes:
        dec=0
        for i in range(0,len(b)):
            if b[i]==1: dec+=pow(2,i)
        f.write(chr(dec))
    f.close()
    return True

print(read_file_data("res"))