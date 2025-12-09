import csv
from PIL import Image
import os

# ==== 設定 ====
CSV_FILE = "input_map_csv.csv"       # 入力 CSV（Shift_JIS）
TEXTURE_DIR = "texture"              # テクスチャ画像フォルダ
OUTPUT_FILE = "input_map.png"        # 出力 PNG
TILE_SIZE = (200, 200)               # 各タイル画像サイズ（200×200）

# ==== 記号 → テクスチャファイル名 の対応表を texture フォルダから自動生成 ====
TILE_MAP = {}

# texture フォルダ内の PNG ファイルを走査
for filename in os.listdir(TEXTURE_DIR):
    # ここで filename は Python 内部では Unicode なので問題ない想定ですが、
    # 念のため str() で文字列化しておく
    filename = str(filename)

    if not filename.lower().endswith(".png"):
        continue

    # 拡張子を除いた部分を「記号」とみなす
    key = os.path.splitext(filename)[0]
    TILE_MAP[key] = filename

# 「＿.png」があれば、空白系の記号をそこに寄せる
placeholder_key = "＿"
if placeholder_key in TILE_MAP:
    placeholder_filename = TILE_MAP[placeholder_key]
    # 空文字列・半角スペース・全角スペースを「＿.png」に対応させる
    TILE_MAP[""] = placeholder_filename
    TILE_MAP[" "] = placeholder_filename
    TILE_MAP["　"] = placeholder_filename
else:
    # プレースホルダーが無い場合の簡易対策
    if TILE_MAP:
        any_filename = next(iter(TILE_MAP.values()))
        TILE_MAP[""] = any_filename
        TILE_MAP[" "] = any_filename
        TILE_MAP["　"] = any_filename
    else:
        # ここで日本語を含めるとコンソールによっては UnicodeError になるので英語にしておく
        raise RuntimeError("No PNG files were found in the texture directory.")

# ==== CSV を読み込む（Shift_JIS / cp932 系） ====
map_data = []
# errors="ignore" を付けると、どうしても読めない文字は飛ばして読み込んでくれます
with open(CSV_FILE, encoding="shift_jis", errors="ignore", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        # 余計な空白を削除（全角スペースも削除したい場合は replace を追加）
        normalized_row = [cell.strip() for cell in row]
        map_data.append(normalized_row)

if not map_data:
    raise RuntimeError("CSV map data is empty or could not be read.")

# マップの行数・列数
rows = len(map_data)
cols = max(len(r) for r in map_data)

# ==== 出力画像のキャンバス作成 ====
output_width = cols * TILE_SIZE[0]
output_height = rows * TILE_SIZE[1]
output_img = Image.new("RGBA", (output_width, output_height))

# ==== タイルの貼り付け ====
for y, row in enumerate(map_data):
    for x, cell in enumerate(row):
        # cell も内部では Unicode なので、念のため str() して扱う
        cell = str(cell)

        # 全角スペースを半角スペースに寄せてから空文字対策
        if cell == "" or cell == " " or cell == "　" or cell == "＿":
            cell = "＿"

        # 未登録の記号は「＿」扱いにする
        if cell in TILE_MAP:
            filename = TILE_MAP[cell]
        else:
            filename = TILE_MAP.get("＿", TILE_MAP.get("", None))

        if filename is None:
            # ここも英語メッセージにしておく
            raise ValueError(f"No texture mapped for symbol: {repr(cell)}")

        texture_path = os.path.join(TEXTURE_DIR, filename)

        if not os.path.exists(texture_path):
            raise FileNotFoundError(f"Texture image not found: {texture_path}")

        tile_img = Image.open(texture_path).convert("RGBA")

        # 貼り付け位置
        px = x * TILE_SIZE[0]
        py = y * TILE_SIZE[1]

        output_img.paste(tile_img, (px, py), tile_img)

# ==== 出力 ====
output_img.save(OUTPUT_FILE)

# コンソールの UnicodeEncodeError を避けるため、英数字だけにする
print("Saved:", OUTPUT_FILE)
