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
with open('list.txt','r') as in_file, open('added_list.txt','a+') as log_read :

    log_read.seek(0)
    # 改行でリストへ分割。さらに左右の空白消去
    urls = list(map(str.strip,(in_file.read().split("\n"))))
    logs = list(map(str.strip,(log_read.read().split("\n"))))

    # リストからURLをひとつづつ処理
    for url in urls :
        # ログファイルにあるか確認
            if url not in logs :
                print('{0}はログにありません'.format(url))
                log_read.write(url + '\n')
            else :
                # ログにあるのでスキップ
                print('{0}は既に記録済みなのでスキップします'.format(url))

