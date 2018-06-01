# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread
from numpy import *

# 画像の読み込み
gazo = imread( "kadai7.bmp", 0 )

# ヒストグラムを表示
figure()
hist( gazo.flatten(), 256, (0,255) )


for y in range(0,358):
    for x in range(0,499):
        # 課題： 6つの図形の面積（画素数）を計算しなさい．
        #      レポートでは計算方法を分かりやすく説明しなさい．
        gazo[y][x] = gazo[y][x]


# 画素値を表示
figure()
imshow(gazo, cmap="gray", vmin=0, vmax=255)
show()
