from PIL import Image
import math

import random

def round_to_up(v):
    if(v-int(v)!=0): return int(v)+1
    return int(v)

def charToBits(char):
    dec=ord(char)
    bits=[]
    while dec!=0:
        b=dec%2
        bits.append(int(b))
        dec-=b
        dec/=2
    while len(bits)<8: bits.append(0)
    return bits

def create_image_from_string(string):
    bytes_count=len(string)
    bits_count=bytes_count*8
    px_width=round_to_up(math.sqrt(bits_count))
    px_height=px_width
    im=Image.new(mode="RGB",size=(px_width,px_height))
    bit_map=[]
    for h in string:
        for b in charToBits(h):
            bit_map.append(b)
    actual_bit=0
    for y in range(0,px_height):
        for x in range(0,px_width):
            if actual_bit>=len(bit_map):
                im.putpixel((x,y),(255,0,0))
            elif (bit_map[actual_bit]):
                im.putpixel((x,y),(255,255,255))
            else:
                im.putpixel((x,y),(0,0,0))
            actual_bit+=1
    return im

def save_data_to_image(name,text):
    create_image_from_string(text).save(f"./result/{name}.png","png")


import json
input=[]

for i in range(1,50000):
    input.append(random.randrange(0,120))

save_data_to_image("res",str(json.dumps(input)))
