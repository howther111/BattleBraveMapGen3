# -*- coding: utf-8 -*-

import sys
import re
from datetime import date
from PIL import Image, ImageDraw, ImageFont, ImageColor


def usage():
    print
    "Usage: python %s image_file [alpha] [fontsize] [fontpath]" % sys.argv[0]


def draw_transparent_text(src_canvas, text, pos, font, fill, alpha):
    mask = Image.new("L", src_canvas.size, 1)
    text_canvas = Image.new("RGB", src_canvas.size, "#000000")
    text_canvas.putalpha(mask)

    draw = ImageDraw.Draw(text_canvas)
    draw.text(pos, text, font=font, fill=fill)
    del draw

    src_canvas.putalpha(mask)
    return Image.blend(src_canvas, text_canvas, alpha).convert("RGB")


def main(path, alpha, fontsize, fontpath, posX=0, posY=0):
    canvas = Image.open(path)
    canvas_size = canvas.size
    font = ImageFont.truetype(fontpath, fontsize, encoding="utf-8")
    text = u"テスト"
    fill = ImageColor.getrgb("white")
    canvas = draw_transparent_text(canvas, text, pos=(posX, posY), font=font,
                                   fill=fill, alpha=alpha)
    canvas.save(sys.stdout, "PNG")


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    else:
        usage()
        sys.exit(1)

    alpha = 0.5
    if len(sys.argv) >= 3:
        alpha = float(sys.argv[2])

    fontsize = 14
    if len(sys.argv) >= 4:
        fontsize = int(sys.argv[3])

    fontpath = "/usr/share/fonts/truetype/mona/mona.ttf"
    if len(sys.argv) >= 5:
        fontsize = sys.argv[5]

    main(path, alpha=alpha, fontsize=fontsize, fontpath=fontpath)