# coding=utf-8
from PIL import Image
import glob
import os
import tinify
tinify.key = "tuH_YrjVJrB1Qz7EoCdSTsT3LsBboska"

# 縮小前の画像があるdir
FROM_DIR = "/Users/kawamataryou/PycharmProjects/cap/images"
# 縮小後の画像を置くdir
TO_DIR = "/Users/kawamataryou/PycharmProjects/cap/min-images"
# 圧縮後の画像を置くdir
MIN_DIR = "/Users/kawamataryou/PycharmProjects/cap/op-images"
# 縮小率
ratio = 0.3

# 縮小
for infile in glob.glob(os.path.join(FROM_DIR, "*.png")):
    im = Image.open(infile)
    im.thumbnail((500,500), Image.ANTIALIAS)
    im.save(os.path.join(TO_DIR, os.path.basename(infile)))

# 無劣化圧縮
for infile in glob.glob(os.path.join(TO_DIR, "*.png")):
    op = tinify.from_file(infile)
    op.to_file(os.path.join(MIN_DIR, os.path.basename(infile)))