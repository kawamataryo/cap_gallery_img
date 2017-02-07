from selenium import webdriver
import os
import time

#変数設定
LOGIN_URL = "http://localhost:8888/clinic/web/wp/wp-login.php"
ID = "ba068082@gmail.com"
PASS = "G#pt(FAnY%@iEG$aog"
IMPORT_URL = "http://localhost:3000/clinic/web/wp/wp-admin/admin.php?import=csv"
IMAGE_URL = "http://localhost:3000/clinic/web/wp/wp-admin/media-new.php"

# プラウザ起動
driver = webdriver.Chrome()

# ----------------------------------------------------
# ログイン
# ----------------------------------------------------

# LOGIN_URLを開く
driver.get(LOGIN_URL)

# ログインID・PASS入力
inp = driver.find_element_by_id("user_login")
inp.clear()
inp.send_keys(ID)
inp = driver.find_element_by_id("user_pass")
inp.clear()
inp.send_keys(PASS)

# フォーム送信
form = driver.find_element_by_id("loginform")
form.submit()
print('ログイン成功')

# ----------------------------------------------------
# csv送信
# ----------------------------------------------------

# インポートにアクセス
driver.get(IMPORT_URL)

# インポートファイルを選択
inp_file = driver.find_element_by_id("upload")
inp_file.send_keys(os.getcwd()+"/upload.csv")

# フォーム送信
form = driver.find_element_by_id("import-upload-form")
form.submit()


# ----------------------------------------------------
# メディアをアップロード
# ----------------------------------------------------

# メディアを追加にアクセス
driver.get(IMAGE_URL)

# メディアを選択
up_image = driver.find_element_by_id("async-upload")
up_image.send_keys(os.getcwd()+"/op-images/heishindou.png")

# フィオームを送信
form_btn = driver.find_element_by_id("html-upload")
form_btn.click()


driver.quit()