# やりたいこと
# list.txtのリストからcsv形式の投稿アップロード用ファイルを作成
# 最初の指定行をカンマ区切りで印字（post_title とかとか）
# list.txtを取得。一行づつ処理
# できればスクレイピングでサイトタイトルを取得したい。


# 画像ファイル名整形関数のインストール
from func import image_name, get_title

#

# 設定項目
INIT_ROW = ['post_title','address','capture','url','post_type']
# 画像のURL
IM_ADRRESS = 'http://localhost:8888/clinic/web/app/uploads/2017/02/'
# 設定する投稿タイプ
POST_TYPE = 'post'

with open('list.txt',mode='r') as inp_f, open('upload.csv',mode='w') as out_f :

    # 設定行の書き込み
    out_f.write(",".join(INIT_ROW))
    out_f.write("\n")

    # list.txtからurlを取得して一つづつ設定s
    for line in inp_f :
        #初期化
        set_row = {
            'title': '',
            'address': '',
            'capture': '',
            'url': '',
            'post_type' : ''
        }
        url = line.strip()

        #タイトル行の追加
        set_row['title'] = get_title(url)

        #画像アドレスの追加
        img_name = image_name(url)
        set_row['capture'] = IM_ADRRESS + img_name

        #URL行の追加
        set_row['url'] = url

        #所在地の設定
        set_row['address'] = '入力待ち'

        #投稿タイプの設定
        set_row['post_type'] = POST_TYPE

        #辞書を結合して書き出し
        out_f.write(','.join(list(set_row.values())))
        out_f.write("\n")