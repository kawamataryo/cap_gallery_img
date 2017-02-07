# やりたいこと
# list.txtのリストからcsv形式の投稿アップロード用ファイルを作成
# 最初の指定行をカンマ区切りで印字（post_title とかとか）
# list.txtを取得。一行づつ処理
# できればスクレイピングでサイトタイトルを取得したい。


# 画像ファイル名整形関数のインストール
from func import image_name, get_title

# 辞書の順番固定
from collections import OrderedDict

# 設定項目
INIT_ROW = ['post_title','address','capture','url','post_type','post_status']
# 画像のURL
IM_ADRRESS = 'http://localhost:8888/clinic/web/app/uploads/2017/02/'
# 設定する投稿タイプ
POST_TYPE = 'post'
POST_STATUS = 'publish'

with open('list.txt',mode='r') as inp_f, open('upload.csv',mode='w') as out_f :

    # 設定行の書き込み
    out_f.write(",".join(INIT_ROW))
    out_f.write("\n")

    # list.txtからurlを取得して一つづつ設定s
    for line in inp_f :
        #初期化
        set_row = []
        url = line.strip()

        #タイトル行の追加
        set_row.append(get_title(url))

        #所在地の設定
        set_row.append('入力待ち')

        #画像アドレスの追加
        img_name = image_name(url)
        set_row.append(IM_ADRRESS + img_name)

        #URL行の追加
        set_row.append(url)

        #投稿タイプの設定
        set_row.append(POST_TYPE)

        #投稿ステータスの設定
        set_row.append(POST_STATUS)

        #辞書を結合して書き出し
        out_f.write(','.join(set_row))
        out_f.write("\n")