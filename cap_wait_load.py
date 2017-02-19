from selenium import webdriver
from func import cap, image_name
from PIL import Image
import glob
import os
import tinify
from tqdm import tqdm


# キーの設定
tinify.key = "RwskgYFv5mvmstHOpfs3ZOtPA9TmPCJO"
# 縮小前の画像があるdir
FROM_DIR = "/Users/kawamataryou/PycharmProjects/cap/images"
# 縮小後の画像を置くdir
MIN_DIR = "/Users/kawamataryou/PycharmProjects/cap/min-images"


# -------------------------------------------------
# キャプチャ取得
# -------------------------------------------------
# URL取得(list.txt)のファイルより
input_txt = open('list.txt','r').read()

# 改行でリストへ分割。さらに左右の空白消去
URLS = list(map(str.strip,(input_txt.split("\n"))))

# プラウザ起動
driver = webdriver.Chrome()
try:
    # リストからURLをひとつづつ処理
    for url in URLS :
        # ドメインの一部をファイル名として設定
        file = image_name(url)
        # キャプチャ保存
        cap(driver, url,FROM_DIR, file, 10)

finally:
    driver.quit()

# -------------------------------------------------
# リサイズ
# -------------------------------------------------

# 縮小切り抜
for infile in tqdm(glob.glob(os.path.join(FROM_DIR, "*.png"))):
    # 画像サイズ変更
    im = Image.open(infile)
    im.crop((0, 0, 590, 335))
    im.thumbnail((600,600), Image.ANTIALIAS)
    #スクロールバーの切り抜き
    im = im.crop((0, 0, 590, 335))
    im.save(os.path.join(MIN_DIR, os.path.basename(infile)))

# 無劣化圧縮
for infile in tqdm(glob.glob(os.path.join(MIN_DIR, "*.png"))):
    # tinypngに接続して圧縮
    op = tinify.from_file(infile)
    op.to_file(os.path.join(MIN_DIR, os.path.basename(infile)))