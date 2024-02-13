from PIL import Image, ImageDraw
import random

def pixel_create(xmax=8, ymax=8, color1="#80CF88", color2="#507A4A", rate=0.2):
    canvas = Image.new("RGB", (xmax, ymax), color1)
    draw = ImageDraw.Draw(canvas)
    for i in range(ymax):
        for j in range(xmax):
            rnd = random.random()
            if rnd <= rate:
                draw.point((i, j), color2)

    #canvas.show()
    return canvas

#pixel_create()