import time
import re
from bs4 import BeautifulSoup
import urllib.request

# -------------------------------------------------
# ファイル名の整形
# -------------------------------------------------

def image_name(url) :
    # URLのドメイン抽出パターン作成
    pat = r"https?://(www.)?([\w-]+).[\w.]"
    # 正規表現でマッチして抽出
    find_list = re.findall(pat, url)
    name = find_list[0][1]
    # png形式にして名前を返す
    return name + ".png"

# -------------------------------------------------
# キャプチャの作成
# -------------------------------------------------
def cap(browser, url, image_dir, file, wait) :
    # URLを開く
    browser.get(url)
    # ウィンドウサイズを設定
    browser.set_window_size(1250, 1036)
    # 読み込み待機
    time.sleep(wait)
    # スクリーンショット取得
    browser.save_screenshot(image_dir + "/" + file)

# -------------------------------------------------
# urlからtitleの取得
# -------------------------------------------------
def get_title(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    title = soup.title.string
    return title

# -------------------------------------------------
# ログの確認、書き込み
# -------------------------------------------------
def log_conf() :
    with open('list.txt','r') as in_file, open('added_list.txt','a+') as log_file:
        # log_fileのポインタを先頭に戻す
        log_file.seek(0)

        # 改行でリストへ分割。さらに左右の空白消去
        urls = list(map(str.strip,(in_file.read().strip().split("\n"))))
        logs = log_file.read().strip()

        # 初期化
        conf_urls = []
        # listがlogにあるか確認。あればスキップ
        for url in urls :
            if url not in logs :
                conf_urls.append(url)
                # ログに書き込み
                log_file.write(url + '\n')
            else :
                print("{0}はログにあるのでスキップします".format(url))

    # 確認後のものをリストを書き出し
    with open('list.txt', 'w') as in_file :
        for conf_url in conf_urls :
            in_file.write(conf_url + "\n")