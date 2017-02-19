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
# URL取得(list.txt)のファイルより読み込み。履歴ファイルも読み込み。
with open('list.txt','r') as in_file, open('added_list.txt','a+') as log_file:

    # log_fileのポインタを先頭に戻す
    log_file.seek(0)

    # 改行でリストへ分割。さらに左右の空白消去
    urls = list(map(str.strip,(in_file.read().split("\n"))))
    logs = list(map(str.strip,(log_file.read().split("\n"))))

    # プラウザ起動
    driver = webdriver.Chrome()
    try:
        # リストからURLをひとつづつ処理
        for url in urls :
            # ログファイルにあるか確認
                if url not in logs :
                    # ドメインの一部をファイル名として設定
                    file = image_name(url)
                    # キャプチャ保存
                    cap(driver, url,FROM_DIR, file, 1)
                    # ログファイルに書き込み
                    log_file.write(url + '\n')
                    print('{0}のキャプチャを保存'.format(url))
                else :
                    # ログにあるのでスキップ
                    print('{0}は既に記録済みなのでスキップします'.format(url))
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