import time
import re
from bs4 import BeautifulSoup
import urllib.request

# -------------------------------------------------
# ファイル名の整形
# -------------------------------------------------

def image_name(url) :
    # URLのドメイン抽出パターン作成
    pat = r"http://([\w-]+).[\w.]+"
    # 正規表現でマッチして抽出
    name = re.search(pat, url).group(1)
    # png形式にして名前を返す
    return name + ".png"

# -------------------------------------------------
# キャプチャの作成
# -------------------------------------------------
def cap(browser, url, file) :
    # URLを開く
    browser.get(url)
    # ウィンドウサイズとズームを設定
    browser.set_window_size(1250, 1036)
    # browser.execute_script("document.body.style.zoom='90%'")
    # 読み込み待機時間
    time.sleep(4)
    # スクリーンショット取得
    browser.save_screenshot("./images/" + file)

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