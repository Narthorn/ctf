#!/usr/bin/python 

import pickle
import numpy as np
import math
from PIL import Image

from collections import defaultdict

from itertools import islice
def batched(iterable, n):
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


projector_width  = 520
projector_length = 330

ceiling = -2800

spot_angle = 8

between_width  = 570
between_length = 670

width_spacing  = between_width + projector_width
length_spacing = between_length + projector_length

min_x = -10000
max_x = 20000

min_y = -10000
max_y = 20000

image_width = 256
image_height = 256

x_resolution = image_width/(max_x-min_x)
y_resolution = image_height/(max_y-min_y)


tilt_axis = [-1,0,0]
pan_axis = [0,0,-1]


projectors = []
for i in range(16):
    y,x = divmod(i,4)
    projectors.append((width_spacing * x, length_spacing * y, ceiling))

def rotation_matrix(axis, theta):
    #honteusement pompé de stackoverflow
    theta = theta/360 * 2*math.pi
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d

    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])
def rotate_projector(dir, pan, tilt):
    vector_tilt_axis = np.dot(rotation_matrix(pan_axis,pan),tilt_axis)
    return np.dot(rotation_matrix(vector_tilt_axis,tilt),np.dot(rotation_matrix(pan_axis,pan),dir))

def raycast(origin, direction, normal=[0,0,-1]):
    if np.dot(direction,normal)**2 < 0.0000001:
        return np.asarray((origin[0], origin[1], 0))
    return origin - np.dot(origin,normal)/np.dot(direction,normal) * direction

with open("data","rb") as f: data = pickle.loads(f.read())

"""
pan = 90
tilt = 0
projector_axes = [rotate_projector(v, pan, tilt) for v in ([0,-1,0], [1,0,0], [0,0,1])]
for v in projector_axes: print(v)
print()

shiftleft = np.dot(rotation_matrix(projector_axes[1], -spot_angle), projector_axes[0])
shiftright = np.dot(rotation_matrix(projector_axes[1], +spot_angle), projector_axes[0])
shifttop = np.dot(rotation_matrix(projector_axes[2], +spot_angle), projector_axes[0])
shiftbottom = np.dot(rotation_matrix(projector_axes[2], -spot_angle), projector_axes[0])

print(shiftleft)
print(shiftright)
print(shifttop)
print(shiftbottom)
print()
left = raycast((5,5,5), shiftleft)
right = raycast((5,5,5), shiftright)
top = raycast((5,5,5), shifttop)
bottom = raycast((5,5,5), shiftbottom)

print(left)
print(right)
print(top)
print(bottom)
print()

print(np.linalg.norm(left-right))
print(np.linalg.norm(top-bottom))

exit()
"""

colormap = [None for _ in range(256)]
for x in range(0,9):     colormap[x] = (255,255,255)  # white
for x in range(9,18):    colormap[x] = (255,0,0)      # red
for x in range(18,26):   colormap[x] = (255,128,0)    # orange
for x in range(26,35):   colormap[x] = (0,255,200)    # cyan-green
for x in range(35,43):   colormap[x] = (0,255,0)      # green
for x in range(43,52):   colormap[x] = (128,255,128)  # light green
for x in range(52,60):   colormap[x] = (128,0,128)    # purple
for x in range(60,69):   colormap[x] = (255,107,95)   # pink
for x in range(69,77):   colormap[x] = (255,255,0)    # yellow
for x in range(77,86):   colormap[x] = (255,165,0)    # magenta
for x in range(86,94):   colormap[x] = (0,255,255)    # cyan
for x in range(94,103):  colormap[x] = (128,128,128)  # CTO 190k (not really)
for x in range(103,111): colormap[x] = (165,165,165)  # CTO 240k (not really)
for x in range(111,120): colormap[x] = (64,64,64)     # CTB 7000k (not really)
for x in range(120,128): colormap[x] = (0,0,255)      # blue

def pprint(x): print([round(v, 2) for v in x])

"""
pprint(rotate_projector([0,-1,0],0,0))
pprint(rotate_projector([0,-1,0],90,0))
pprint(rotate_projector([0,-1,0],180,0))
pprint(rotate_projector([0,-1,0],270,0))
pprint(rotate_projector([0,-1,0],360,0))
print()

pprint(rotate_projector([0,-1,0],0,0))
pprint(rotate_projector([0,-1,0],0,90))
pprint(rotate_projector([0,-1,0],0,180))
pprint(rotate_projector([0,-1,0],0,270))
pprint(rotate_projector([0,-1,0],0,360))
print()

pprint(rotate_projector([0,-1,0],30,0))
pprint(rotate_projector([0,-1,0],30,90))
pprint(rotate_projector([0,-1,0],30,180))
pprint(rotate_projector([0,-1,0],30,270))
pprint(rotate_projector([0,-1,0],30,360))
print()

exit()

"""
"""
pan_values = set()
tilt_values = set()
for frame in data:
    for i,(color, brightness, focus, pan, pan_fine, tilt, tilt_fine, reset) in enumerate(batched(frame,n=8)):
        pan_values.add((256*pan+pan_fine)/(256**2) * 540)
        tilt_values.add((256*tilt+tilt_fine)/(256**2) * 270)

print(sorted(pan_values))
print(sorted(tilt_values))
"""

"""
def add_point(px,p,brightness,color, thickness=0):
    x,y,_ = p
    if x < min_x or max_x <= x: return
    if y < min_y or max_y <= y: return
    px_x = (x-min_x)*x_resolution
    px_y = (y-min_y)*y_resolution
    for dx in range(-thickness, thickness+1):
       if px_x+dx < 0 or image_width <= px_x+dx: continue
       for dy in range(-thickness, thickness+1):
            if px_y+dy < 0 or image_height <= px_y+dy: continue
            px[px_x+dx,px_y+dy] = tuple(int(k) for k in brightness/255*np.asarray(colormap[color]))
"""

def add_point(px,p, color):
    x,y,_ = p
    if x < min_x or max_x <= x: return
    if y < min_y or max_y <= y: return
    px_x = int((x-min_x)*x_resolution)
    px_y = int((y-min_y)*y_resolution)
    px[px_x,px_y].append(color)

n_frames = len(data)

current_dirs = None

F_pan_tilt = [
    (177.2396, 120.5081, 10),
    (179.7610, 121.5093, 10),
    (177.2396, 119.5111, 10),
    (173.5976, 120.5081, 10),
    (173.5976, 126.4450, 10),
    (84.9778,  128.4431, 10),
    (91.1412,  128.4431, 10),
    (89.5592,  127.4461, 10),
    (177.2396, 112.5113, 87),
    (110.5708, 121.5093, 87),
    (122.8894, 123.5074, 87),
    (135.2163, 124.5086, 87),
    (160.8093, 131.4424, 87),
    (50.7082,  126.4450, 87),
    (17.8393,  129.4443, 87),
    (14.8482,  129.4443, 87),
]


C_pan_tilt = [
    (179.7610, 118.5100, 10),
    (175.1879, 118.5100, 10),
    (173.5976, 119.5111, 10),
    (167.4424, 120.5081, 10),
    (179.7610, 121.5093, 9),
    (116.2646, 127.4461, 9),
    (108.0412, 126.4450, 9),
    (103.9377, 126.4450, 9),
    (169.4942, 123.5074, 87),
    (158.7494, 113.5125, 87),
    (160.3397, 113.5125, 87),
    (158.7494, 113.5125, 87),
    (166.9728, 125.5097, 87),
    (169.0245, 125.5097, 87),
    (171.0762, 125.5097, 87),
    (171.5459, 124.5086, 87),
]

frames = []
bg_color = (0,0,0)
fg_color = (255,255,255)

"""
from PIL import ImageDraw

spot_angle=4

#letter, pan_tilt= ("C", C_pan_tilt)
letter, pan_tilt= ("F", F_pan_tilt)
min_tilt_offset = -50
max_tilt_offset = -50
min_pan_offset = -100
max_pan_offset = 100
PAN_SAMPLES = 200
TILT_SAMPLES = 1
for pan_t in range(PAN_SAMPLES):
    for tilt_t in range(TILT_SAMPLES):
        print(f"{pan_t*TILT_SAMPLES+tilt_t}/{PAN_SAMPLES*TILT_SAMPLES-1}")
        im = Image.new('RGB', (image_width, image_height), color=bg_color)
        px = im.load()
        px_samples = defaultdict(list)
        pan_offset = min_pan_offset + pan_t/PAN_SAMPLES * (max_pan_offset-min_pan_offset)
        tilt_offset = min_tilt_offset + tilt_t/TILT_SAMPLES * (max_tilt_offset-min_tilt_offset)
        for i,(pan,tilt,color) in enumerate(pan_tilt):
            pan = pan_offset + pan
            tilt = tilt_offset + tilt
            color = colormap[color]
            #color = colormap[int(i/16*128)]

            pos = projectors[i]
            projector_axes = [rotate_projector(v, pan, tilt) for v in ([0,1,0], [-1,0,0], [0,0,1])]
            for lr_angle in range(-spot_angle, spot_angle+1):
                for tb_angle in range(-spot_angle, spot_angle+1):
                    if lr_angle**2 + tb_angle**2 > spot_angle**2: continue
                    point = raycast(pos, np.dot(rotation_matrix(projector_axes[1],tb_angle),np.dot(rotation_matrix(projector_axes[2],lr_angle),projector_axes[0])))
                    add_point(px_samples, point, color)

        for point,colors in px_samples.items():
            if len(set(colors)) > 1: continue
            px[point] = tuple(colors[0])
            #px[point] = tuple(int(min(255,k)) for k in sum(colors))
            #px[point] = tuple(int(k) for k in sum(colors)/len(colors))

        d = ImageDraw.Draw(im)
        d.text((2,2), f"pan: {round(pan_offset,2)}", fill=fg_color)
        d.text((2,14), f"tilt: {round(tilt_offset,2)}", fill=fg_color)
        d.text((2,26), letter, fill=fg_color)

        frames.append(im)

"""

for k,frame in enumerate(data):
#for k,frame in enumerate(data[:200]):
#for k,frame in enumerate(data[:700]):
    im = Image.new('RGB',(image_width,image_height), bg_color)
    px = im.load()
    px_samples = defaultdict(list)

    current_dir = []

    print(f"{k}/{n_frames-1}")
    for i,(color, brightness, focus, pan, pan_fine, tilt, tilt_fine, reset) in enumerate(batched(frame,n=8)):
        #if i != 0: continue

        if i >= len(projectors): continue
        assert focus == 0, focus
        assert reset == 0, reset
        pos = projectors[i]

        pan = (pan*256+pan_fine)/((256**2)-1) * 540 
        tilt = (tilt*256+tilt_fine)/((256**2)-1) * 270 -53

        projector_axes = [rotate_projector(v, pan, tilt) for v in ([0,1,0], [-1,0,0], [0,0,1])]
        current_dir.append((i,tuple(round(k,2) for k in projector_axes[0]),pan, tilt, color))

        if brightness == 0: continue
        elif brightness == 255: color = colormap[color]
        #elif brightness == 255: color = np.asarray((256*pan/350,256*(tilt-101)/(165-101),0))
        #elif brightness == 255: color = colormap[int(i/16*128)]
        else: assert False


        for lr_angle in range(-spot_angle, spot_angle+1):
            for tb_angle in range(-spot_angle, spot_angle+1):
                if lr_angle**2 + tb_angle**2 > spot_angle**2: continue
                point = raycast(pos, np.dot(rotation_matrix(projector_axes[1],tb_angle),np.dot(rotation_matrix(projector_axes[2],lr_angle),projector_axes[0])))
                add_point(px_samples, point, color)

    #    for px_y in range(image_height):
    #        y = min_y+px_y/y_resolution
    #        for px_x in range(image_width):
    #            x = min_x+px_x/x_resolution

    #            if np.linalg.norm((x,y,0) - c) < max(1/x_resolution,1/y_resolution): 
    #            #p = (x, y,0)-c
    #            #if np.dot(p,left-right)**2 < 0.1 or np.dot(p, top-bottom)**2 < 0.1:
    #                px[px_x,px_y] = tuple(int(k) for k in brightness/255*np.asarray(colormap[color]))

    if current_dirs != current_dir:
        current_dirs = current_dir
        for (i, pos, pan, tilt, color) in current_dirs:
            print(f"{i}: {pos} - pan: {pan:.4f} - tilt: {tilt:.4f} - color: {color}")

    for point,colors in px_samples.items():
        #if len(set(colors)) > 1: continue
        #px[point] = tuple(colors[0])
        px[point] = tuple(min(255,k) for k in sum(np.asarray(c) for c in colors))
        #px[point] = tuple(int(k) for k in sum(colors)/len(colors))

    frames.append(im)



frames[0].save("dazzled.gif", save_all=True, append_images=frames[1:], duration=20, loop=0)

