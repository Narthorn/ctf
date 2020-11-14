#!/usr/bin/python3
from PIL import Image
import re

src = Image.open("flag.png")
srcpixels = src.getdata()

bitstring = ''.join(f'{r:08b}{g:08b}{b:08b}' for (r,g,b,a) in srcpixels)

data_size = len(bin(len(srcpixels)*8*3))-2 # datasizebit

number_of_offsets = int(bitstring[:data_size],2)

length_size = int(bitstring[data_size:2*data_size],2)

offsets = []
for i in range(number_of_offsets):
   offset = bitstring[2*data_size + i*(data_size+length_size)          :2*data_size + i*(data_size+length_size) + data_size]
   length = bitstring[2*data_size + i*(data_size+length_size)+data_size:2*data_size + i*(data_size+length_size) + data_size+length_size]
   offsets.append((int(offset,2),int(length,2)))

base_offset = (len(srcpixels)*8*3)//4

out = ''.join(bitstring[base_offset+o:base_offset+o+n] for (o,n) in offsets)   
print(int(out,2).to_bytes((len(out)+7)//8, byteorder='big'))

# figuring out base_offset without actually knowing it:

for match in re.finditer(''.join(f'{ord(c):08b}' for c in "DGS")[:19], bitstring):
      out = ""
      base_offset = match.start(0)-offsets[0][0]
      for (o,n) in offsets:
          out += bitstring[base_offset+o:base_offset+o+n]
      print(base_offset, int(out,2).to_bytes((len(out)+7)//8, byteorder='big'))
