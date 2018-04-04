# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread

# 画像の読み込み
gazo = imread( "hello_world.png", 0 )

# 画素値を表示
print gazo

# 画素値を表示
imshow(gazo, interpolation="None" ,cmap="gray", vmin=0, vmax=255)
show()
