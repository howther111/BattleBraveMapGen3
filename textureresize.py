import os
from PIL import Image

# 元画像フォルダと保存先フォルダ
src_dir = "texture_1024"
dst_dir = "texture_200"

# 保存先フォルダが無ければ作成
os.makedirs(dst_dir, exist_ok=True)

# フォルダ内のファイルを順番に処理
for filename in os.listdir(src_dir):
    # PNG だけ対象にする（大文字拡張子にも対応）
    if not filename.lower().endswith(".png"):
        continue

    src_path = os.path.join(src_dir, filename)
    dst_path = os.path.join(dst_dir, filename)

    # 画像を開いて 200x200 にリサイズ
    with Image.open(src_path) as img:
        # アスペクト比は無視して 200x200 に縮小（もしくは拡大）
        resized = img.resize((200, 200), Image.LANCZOS)
        # 同じファイル名で PNG として保存
        resized.save(dst_path, format="PNG")

print("変換が完了しました。")