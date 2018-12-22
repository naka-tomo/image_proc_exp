# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread
import random
import numpy as np
import cv2

# 画像を読み込み
gazo = imread( "kadai8.bmp", 0 )

gazo[gazo==76] = 50
gazo[gazo==122] = 100
gazo[gazo==164] = 150
gazo[gazo==229] = 250

rnd = range(10,40) + range(60,90) + range(110,140)+range(160,190) + range(210,240)


for x in range(0,gazo.shape[1]):
    for y in range(0,gazo.shape[0]):
        if gazo[y][x]>=251:
            r = random.sample( rnd, 1 )[0]
            gazo[y][x] = r

cv2.imwrite("test.bmp", gazo)

        
# 画像を表示
imshow(gazo, cmap="gray", vmin=0, vmax=255, interpolation="None")


figure()
hist( gazo.flatten(), 256, (0,255) )

show()
