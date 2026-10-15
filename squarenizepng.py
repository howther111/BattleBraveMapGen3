
from pathlib import Path
from PIL import Image

# このプログラムが置かれたフォルダ
folder = Path(__file__).resolve().parent

# 保存先フォルダを作成
output_folder = folder / "square_output"
output_folder.mkdir(exist_ok=True)

# 同じフォルダ内のPNG画像を一括処理
for file in folder.iterdir():
    if not file.is_file() or file.suffix.lower() != ".png":
        continue

    with Image.open(file) as img:
        img = img.convert("RGBA")

        width, height = img.size

        # 長い方の辺を正方形の一辺にする
        size = max(width, height)

        # 透明な正方形キャンバス
        square = Image.new(
            "RGBA", (size, size), (0, 0, 0, 0)
        )

        # 元画像を中央に配置
        x = (size - width) // 2
        y = (size - height) // 2

        square.paste(img, (x, y))

        # PNG形式で保存
        output_path = output_folder / file.name
        square.save(output_path)

        print(f"{file.name} → {size}×{size}")

print("すべての画像の正方形化が完了しました。")
