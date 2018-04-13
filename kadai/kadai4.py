# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread

# 画像を読み込み
gazo = imread( "kadai4.bmp", 0 )

print "元画像"
print gazo

# 画像を表示
imshow(gazo, cmap="gray", vmin=0, vmax=255, interpolation="None")

# 画像を変換
gazo2 = zeros((12,12))
for x in range(1,11):
    for y in range(1,11):
        # 課題：filterの値を変えて様々なフィルタを作成し，画素値と画像の変化を確認しなさい．
        #      レポートでは原理（数式）と実行結果を照らし合わせて，それらフィルタの処理を分かりやすく説明しなさい．
        filter = [
            [0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0]
            ]

        gasochi = 0
        for xx in range(3):
            for yy in range(3):
                # ここでfilterの値をgazoに掛ける
                gasochi += gazo[y+yy-1][x+xx-1]

        # 0以下を切り捨てる
        gasochi = int(gasochi) 
        if gasochi<0:
            gasochi =0
        gazo2[y][x] = gasochi

print "変換後の画像"
print gazo2

# 画像を表示
figure()
imshow(gazo2, cmap="gray", vmin=0, vmax=255, interpolation="None")
show()
