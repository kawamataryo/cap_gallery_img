from selenium import webdriver
import os
import glob
import shutil
from tqdm import tqdm

#変数設定
IMAGE_INP = "/Users/kawamataryou/PycharmProjects/cap/min-images"
LOGIN_URL = "http://clinic/wp-login.php"
ID = "ryo"
PASS = "OORBoWQ&^D9WV8nB"
IMPORT_URL = "http://clinic/wp-admin/admin.php?import=csv"
IMAGE_OUT = "/Users/kawamataryou/vagrant-clinic/wordpress/wp-content/themes/sage-8.5/dist/images"

# プラウザ起動
driver = webdriver.Chrome()
try:

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

    # ----------------------------------------------------
    # csv送信
    # ----------------------------------------------------

    # インポートにアクセス
    driver.get(IMPORT_URL)

    # インポートファイルを選択
    inp_file = driver.find_element_by_id("upload")
    inp_file.send_keys(os.getcwd()+"/up-list.csv")

    # フォーム送信
    form = driver.find_element_by_id("import-upload-form")
    form.submit()


    # ----------------------------------------------------
    # メディアをアップロード
    # ----------------------------------------------------
    # フォルダ全てをアップロード
    for image_pass in tqdm(glob.glob(os.path.join(IMAGE_INP, "*.png"))):

        # 画像をwordpressテーマの公開ディレクトリへ移動
        shutil.copy(image_pass, IMAGE_OUT)


finally:

    driver.quit()