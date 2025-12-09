import csv
from PIL import Image
import os
import metaga_mapchip_list

# ==== 設定 ====
CSV_FILE = "input_map_csv.csv"       # 入力 CSV（Shift_JIS）
TEXTURE_DIR = "texture"              # テクスチャ画像フォルダ
OUTPUT_FILE = "input_map.png"        # 出力 PNG
TILE_SIZE = (200, 200)               # 各タイル画像サイズ（200×200）

# 記号 → テクスチャファイル名 の対応表
mapchip_list = metaga_mapchip_list.mapchip_list
TILE_MAP = {}

for key in mapchip_list:
    if key == "　":  # 全角スペース
        TILE_MAP[key] = "　.png"
    else:
        TILE_MAP[key] = f"{key}.png"

# 空文字列も空白扱いにする
TILE_MAP[""] = "　.png"
TILE_MAP[" "] = "　.png"

# ==== CSV を読み込む（Shift_JIS） ====
map_data = []
with open(CSV_FILE, encoding="shift_jis") as f:
    reader = csv.reader(f)
    for row in reader:
        # 余計な空白を削除
        normalized_row = [cell.strip() for cell in row]
        map_data.append(normalized_row)

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

        # 空文字対策
        if cell == "" or cell == " ":
            cell = "　"

        # 未登録の記号は空白扱いにする
        filename = TILE_MAP.get(cell, TILE_MAP["　"])
        texture_path = os.path.join(TEXTURE_DIR, filename)

        if not os.path.exists(texture_path):
            texture_path = os.path.join(TEXTURE_DIR, "　.png")
            #raise FileNotFoundError(f"テクスチャ画像が見つかりません: {texture_path}")

        tile_img = Image.open(texture_path).convert("RGBA")

        # 貼り付け位置
        px = x * TILE_SIZE[0]
        py = y * TILE_SIZE[1]

        output_img.paste(tile_img, (px, py), tile_img)

# ==== 出力 ====
output_img.save(OUTPUT_FILE)
print(f"出力しました: {OUTPUT_FILE}")