
import sys
from pathlib import Path
from PIL import Image


def get_base_folder():
    """exeファイル、またはpyファイルのあるフォルダを取得"""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    return Path(__file__).resolve().parent


def main():
    base_folder = get_base_folder()

    # 入力・出力フォルダ
    input_folder = base_folder / "input"
    output_folder = base_folder / "output"

    # フォルダがなければ自動作成
    input_folder.mkdir(exist_ok=True)
    output_folder.mkdir(exist_ok=True)

    # inputフォルダ内のPNGを取得
    png_files = sorted([
        f for f in input_folder.iterdir()
        if f.is_file() and f.suffix.lower() == ".png"
    ])

    print("=== SquarenizePNG ===")
    print(f"入力フォルダ: {input_folder}")
    print(f"出力フォルダ: {output_folder}")
    print("-------------------------")

    if not png_files:
        print("inputフォルダにPNG画像がありません。")
        print("PNG画像を入れて再実行してください。")
        return

    success = 0
    errors = 0

    for file in png_files:
        try:
            with Image.open(file) as img:
                img = img.convert("RGBA")

                width, height = img.size

                # 長い方の辺を正方形の一辺にする
                size = max(width, height)

                # 透明な正方形キャンバス
                square = Image.new(
                    "RGBA",
                    (size, size),
                    (0, 0, 0, 0)
                )

                # 元画像を中央に配置
                x = (size - width) // 2
                y = (size - height) // 2

                square.paste(img, (x, y))

                # outputフォルダに保存
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

    print("\n=========================")
    print("処理が完了しました。")
    print(f"成功: {success}枚")
    print(f"エラー: {errors}枚")
    print(f"保存先: {output_folder}")
    print("=========================")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"予期しないエラー: {e}")

    input("\nEnterキーを押すと終了します...")
