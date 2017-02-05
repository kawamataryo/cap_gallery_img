import os
import glob


# 縮小前の画像があるdir
FROM_DIR = "/Users/kawamataryou/PycharmProjects/cap/images"
# 縮小後の画像を置くdir
TO_DIR = "/Users/kawamataryou/PycharmProjects/cap/min-images"
# 圧縮後の画像を置くdir
MIN_DIR = "/Users/kawamataryou/PycharmProjects/cap/op-images"

#画像フォルダのクリア
for infile in glob.glob(os.path.join(FROM_DIR, "*.png")):
    os.remove(infile)

for infile in glob.glob(os.path.join(TO_DIR, "*.png")):
    os.remove(infile)

for infile in glob.glob(os.path.join(MIN_DIR, "*.png")):
    os.remove(infile)

# csv、listの初期化
list_f = open('list.txt', mode='w')
list_f.write('')

csv_f = open('upload.csv', mode='w')
csv_f.write('')