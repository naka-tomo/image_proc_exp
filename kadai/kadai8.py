# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread
from numpy import *

# 画像の読み込み
gazo = imread( "kadai8.bmp", 0 )

# ヒストグラムを表示
figure()
hist( gazo.flatten(), 256, (0,255) )

# 課題： 6つの図形の輪郭線の長さ（画素数）を計算しなさい．
#      レポートでは計算方法を分かりやすく説明しなさい．
# ヒント：　二段階の処理が必要．．．
gazo2 = zeros( (358,499) )
for y in range(1,357):
    for x in range(1,498):
        gazo2[y][x] = gazo[y][x]


gazo3 = zeros( (358,499) )
for y in range(1,357):
    for x in range(1,498):
        gazo3[y][x] = gazo2[y][x]



# 画素値を表示
figure()
imshow(gazo, cmap="gray", vmin=0, vmax=255)
figure()
imshow(gazo2, cmap="gray", vmin=0, vmax=255)
figure()
imshow(gazo3, cmap="gray", vmin=0, vmax=255)

show()
