# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread

# 真っ黒の画像を生成
gazo = zeros( (10,10) )

# 画素値を表示
print "画素値"
print gazo

# 画像を表示
imshow(gazo, cmap="gray", vmin=0, vmax=255)

# 課題：配列のインデックスの数字（以下の）例では3と7)を変えて，
#     これらの数字と画像との対応がどのようになっているか確認しなさい．
gazo[3][7] = 255

print "変換後の画像"
print gazo

# 画像を表示
figure()
imshow(gazo, cmap="gray", vmin=0, vmax=255)
show()
