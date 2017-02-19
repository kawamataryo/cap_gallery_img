# coding=utf-8
from PIL import Image
import glob
import os
import tinify

# キーの設定
tinify.key = "RwskgYFv5mvmstHOpfs3ZOtPA9TmPCJO"

# 縮小前の画像があるdir
FROM_DIR = "/Users/kawamataryou/PycharmProjects/cap/images"
# 縮小後の画像を置くdir
MIN_DIR = "/Users/kawamataryou/PycharmProjects/cap/min-images"


# 縮小切り抜き
for infile in glob.glob(os.path.join(FROM_DIR, "*.png")):
    # 画像サイズ変更
    im = Image.open(infile)
    im.crop((0, 0, 590, 335))
    im.thumbnail((600,600), Image.ANTIALIAS)
    #スクロールバーの切り抜き
    im = im.crop((0, 0, 590, 335))
    im.save(os.path.join(MIN_DIR, os.path.basename(infile)))

# 無劣化圧縮
for infile in glob.glob(os.path.join(MIN_DIR, "*.png")):
    # tinypngに接続して圧縮
    op = tinify.from_file(infile)
    op.to_file(os.path.join(MIN_DIR, os.path.basename(infile)))