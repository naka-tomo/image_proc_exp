# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread
from numpy import *

# 画像の読み込み
gazo = imread( "test4.bmp", 0 )


# 課題： 6つの図形の輪郭線の長さ（画素数）を計算しなさい．
#      レポートでは計算方法を分かりやすく説明しなさい．


# 画素値を表示
imshow(gazo, cmap="gray", vmin=0, vmax=255)
show()
