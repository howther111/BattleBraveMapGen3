
import sys
from pathlib import Path
from PIL import Image


def get_base_folder():
    # exe化されている場合
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    # Pythonスクリプトとして実行する場合
    return Path(__file__).resolve().parent


def main():
    folder = get_base_folder()

    # 出力先フォルダ
    output_folder = folder / "square_output"
    output_folder.mkdir(exist_ok=True)

    # PNGファイル一覧
    png_files = [
        f for f in folder.iterdir()
        if f.is_file() and f.suffix.lower() == ".png"
    ]

    if not png_files:
        print("PNG画像が見つかりませんでした。")
        return

    success = 0
    errors = 0

    for file in png_files:
        try:
            with Image.open(file) as img:
                img = img.convert("RGBA")

                width, height = img.size

                # 長い方の辺に合わせる
                size = max(width, height)

                # 透明な正方形キャンバス
                square = Image.new(
                    "RGBA",
                    (size, size),
                    (0, 0, 0, 0)
                )

                # 中央に配置
                x = (size - width) // 2
                y = (size - height) // 2

                square.paste(img, (x, y))

                # 保存
                output_path = output_folder / file.name
                square.save(output_path, "PNG")

                print(
                    f"完了: {file.name} "
                    f"({width}x{height} → {size}x{size})"
                )

                success += 1

        except Exception as e:
            print(f"エラー: {file.name} - {e}")
            errors += 1

    print("\n-------------------------")
    print(f"処理成功: {success}枚")
    print(f"エラー: {errors}枚")
    print(f"保存先: {output_folder}")
    print("-------------------------")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"予期しないエラー: {e}")

    input("\nEnterキーを押すと終了します...")
