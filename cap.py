import time
import re
from selenium import webdriver

# ファイル名の整形
def image_name(url) :
    # URLのドメイン抽出パターン作成
    pat = r"https?://([\w-]+).[\w.]+"
    # 正規表現でマッチして抽出
    name = re.search(pat, url).group(1)
    # png形式にして名前を返す
    return name + ".png"


# キャプチャの作成
def cap(browser, url, file) :
    # URLを開く
    browser.get(url)
    # ウィンドウサイズとズームを設定
    browser.set_window_size(1250, 1036)
    # 読み込み待機時間
    time.sleep(4)
    # スクリーンショット取得
    browser.save_screenshot("./images/" + file)



# URL取得(list.txt)のファイルより
input_txt = open('list.txt','r').read()

# 開業でリストへ分割。さらに左右の空白消去
URLS = list(map(str.strip,(input_txt.split("\n"))))

# プラウザ起動
driver = webdriver.Chrome()

# リストからURLをひとつづつ処理
for url in URLS :
    # ドメインの一部をファイル名として設定
    file = image_name(url)
    # キャプチャ保存
    cap(driver, url, file)


driver.quit()