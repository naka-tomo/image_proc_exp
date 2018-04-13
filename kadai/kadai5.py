# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread

# 画像を読み込み
gazo = imread( "kadai5.bmp", 0 )

# 画像を表示
imshow(gazo, cmap="gray", vmin=0, vmax=255, interpolation="None")

# ヒストグラムを表示
figure()
hist( gazo.flatten(), 256, (0,255) )

# 画像を変換
gazo2 = zeros((240,384))
for x in range(384):
    for y in range(240):
        # 課題：濃度ヒストグラムを参照して，画像の特徴を表わす二値画像を生成しなさい．
        #      レポートでは，作成したプログラムによってどのような処理が行われているのかを
        #      ヒストグラムを使って分かりやすく説明しなさい．
        if gazo[y][x]<0:
            gazo2[y][x] = 0
        else:
            gazo2[y][x] = 0

# 画像を表示
figure()
imshow(gazo2, cmap="gray", vmin=0, vmax=255, interpolation="None")
show()
