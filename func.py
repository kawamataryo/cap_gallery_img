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

