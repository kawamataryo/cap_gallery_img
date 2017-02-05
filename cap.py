from selenium import webdriver


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