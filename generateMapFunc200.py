from PIL import Image, ImageDraw, ImageFont
import settings
import numToAlpha
import tkinter.messagebox as messagebox
#import csv
import matplotlib.colors as mcolors
import sys

def draw_transparent_text(src_canvas, text, pos, font, fill, alpha):
    mask = Image.new("L", src_canvas.size, 1)
    text_canvas = Image.new("RGB", src_canvas.size, "#000000")
    text_canvas.putalpha(mask)

    draw = ImageDraw.Draw(text_canvas)
    draw.text(pos, text, font=font, fill=fill)
    del draw

    src_canvas.putalpha(mask)
    return Image.blend(src_canvas, text_canvas, alpha).convert("RGB")


def generateMapFunc200(xMaxInt, yMaxInt, color="#FFFFFF"):
    print("Program Start")

    color_name = color
    # color_name = 'red'
    color_rgb = tuple(int(c * 255) for c in mcolors.to_rgb(color_name))
    print(color_rgb)  # (160, 79, 0)

    #csvFlg = settings.csvFlg

    # マップサイズ読込
    xMax = xMaxInt
    yMax = yMaxInt

    cellSize = settings.pixelSize * settings.cellNum
    midashiSize = settings.pixelSize * settings.cellNum
    xSize = xMax * cellSize + midashiSize
    ySize = yMax * cellSize + midashiSize
    lineWidth = (settings.pixelSize // 40) * settings.cellNum
    fontsize = int((settings.pixelSize) * settings.cellNum * 0.5)

    im = Image.new('RGBA', (xSize, ySize), (0, 0, 0, 0))
    #backgrouwnIm = Image.open(settings.backgroundImg)
    #im.paste(backgrouwnIm, (midashiSize, midashiSize))
    draw = ImageDraw.Draw(im)
    draw.line((0, 0, 0, ySize), fill=color, width=lineWidth)
    draw.line((0, 0, xSize, 0), fill=color, width=lineWidth)
    font = ImageFont.truetype('C:/Windows/Fonts/meiryo.ttc', fontsize)

    # 升目描画
    for x in range(xMax + 1):
        xZahyo = x * cellSize + midashiSize
        draw.line((xZahyo, 0, xZahyo, ySize), fill=color, width=lineWidth)

    for y in range(yMax + 1):
        yZahyo = y * cellSize + midashiSize
        draw.line((0, yZahyo, xSize, yZahyo), fill=color, width=lineWidth)

    # 文字描画
    num = 1
    for x in range(xMax):
        xPoint = midashiSize + (cellSize / 2) + (x * cellSize)
        yPoint = midashiSize / 2
        w, h = draw.textsize(str(num), font)
        # print(w)
        # print(h)
        draw.text((xPoint - (w / 2), yPoint - (h / 2) - (4 * settings.cellNum)), str(num), fill=color, font=font)
        num = num + 1

    num = 1
    for y in range(yMax):
        xPoint = (midashiSize / 2)
        yPoint = midashiSize + (cellSize / 2) + (y * cellSize)
        alphaNum = ""
        numJyu = num // 26
        numIchi = num % 26
        if numJyu <= 0:
            alphaNum = numToAlpha.numToAlphaOne(numIchi)
        elif numJyu <= 26:
            alphaNum = numToAlpha.numToAlphaOne(numJyu) + numToAlpha.numToAlphaOne(numIchi)
        else:
            messagebox.showinfo('エラー', '縦スクウェアが上限（675）を超えています')
            sys.exit()

        w, h = draw.textsize(alphaNum, font)
        draw.text((xPoint - (w / 2), yPoint - (h / 2) - (4 * settings.cellNum)), alphaNum, fill=color, font=font)
        num = num + 1

    im.save(settings.outputImg)
    print("Program End")
    messagebox.showinfo('生成完了', '出力しました')