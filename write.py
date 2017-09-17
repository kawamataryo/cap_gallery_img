# 画像ファイル名整形関数のインストール
from func import image_name, get_title
#プログレスバー表示
from tqdm import tqdm
import codecs



# 設定項目
INIT_ROW = ['post_title','post_category','capture','url','post_type','post_status']
# 画像のURL
IM_ADRRESS = 'http://clinic/wp-content/themes/sage-8.5/dist/images/'
# 設定する投稿タイプ
POST_TYPE = 'post'
POST_STATUS = 'publish'

# -------------------------------------------------
# カテゴリーの取得
# -------------------------------------------------s

def get_category(title) :
    category = []
    if '鍼灸' in title or '灸' in title or 'はり' in 'きゅう' in title:
        category.append('shinkyu')
    if '整骨' in title :
        category.append('seikotsu')
    if '整体' in title :
        category.append('seitai')
    if '訪問マッサージ' in title :
        category.append('houmon_masa')
    elif 'マッサージ' in title :
        category.append('masa')
    if 'リラクゼーション' in title :
        category.append('rira')
    if '介護' in title:
        category.append('kaigo')
    if '訪問看護' in title:
        category.append('hou_kan')
    if 'カイロプラクティック' in title :
        category.append('kairo')
    if 'アロマ' in title :
        category.append('aroma')
    if '接骨' in title :
        category.append('sekkotsu')
    if not category :
        category.append('other')

    conma = '"'
    result = conma + ','.join(category) + conma
    return result

# -------------------------------------------------
# タイトルの整形
# -------------------------------------------------
# seoでタイトルにキーワードを入れている場合に店名のみ取り出すために入力
def form_title(title) :
    print("抽出タイトル：\n",title)
    f_title = input("店名を入力してください:\n")
    return f_title

# -------------------------------------------------
# メイン
# -------------------------------------------------

with codecs.open('list.txt',mode='r') as inp_f, codecs.open('up-list.csv',mode='w') as out_f :
    # 設定行の書き込み
    out_f.write(",".join(INIT_ROW))
    out_f.write("\n")

    # list.txtからurlを取得して一つづつ設定
    for line in tqdm(inp_f) :
        #初期化
        set_row = []
        url = line.strip()

        #タイトル行の追加
        title = get_title(url)
        f_title = form_title(title)
        set_row.append(f_title)

        #カテゴリーの追加
        category = get_category(title)
        set_row.append(category)

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