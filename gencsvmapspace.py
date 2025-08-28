import random

import pixelCreate
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

#線形補間と連続性を生み出す子たち
def fade(t):return 6*t**5-15*t**4+10*t**3
def lerp(a,b,t):return a+fade(t)*(b-a)

#本体
def perlin(r,seed=np.random.randint(0,2147483647)):
    print("seed=" + str(seed))
    np.random.seed(seed)

    ri = np.floor(r).astype(int) #整数部、インデックスとして使用
    ri[0] -= ri[0].min()         #
    ri[1] -= ri[1].min()         #インデックスとして使用するための準備
    rf = np.array(r) % 1         #小数部
    g = 2 * np.random.rand(ri[0].max()+2,ri[1].max()+2,2) - 1 #格子点の勾配
    e = np.array([[[[0,0],[0,1],[1,0],[1,1]]]])                       #四隅
    er = (np.array([rf]).transpose(2,3,0,1) - e).reshape(r.shape[1],r.shape[2],4,1,2) #四隅の各点から見た位置ベクトル
    gr = np.r_["3,4,0",g[ri[0],ri[1]],g[ri[0],ri[1]+1],g[ri[0]+1,ri[1]],g[ri[0]+1,ri[1]+1]].transpose(0,1,3,2).reshape(r.shape[1],r.shape[2],4,2,1) #おなじみファンシーソートで四隅の勾配をまとめて内積計算できる形に加工
    p = (er@gr).reshape(r.shape[1],r.shape[2],4).transpose(2,0,1) #全点まとめて勾配との内積計算

    return lerp(lerp(p[0],p[2],rf[0]),lerp(p[1],p[3],rf[0]),rf[1]) #補間して返す

def landsea(pery):
    output = pery.copy()
    ymaxtap = pery.shape
    xmaxtap = pery[0].shape
    print(ymaxtap)
    print(xmaxtap)
    ymax = ymaxtap[0]
    xmax = xmaxtap[0]
    print(ymax)
    print(xmax)
    for y in range(ymax):
        for x in range(xmax):
            if pery[y][x] < -0.5:
                output[y][x] = 0
            elif pery[y][x] < -0.3:
                output[y][x] = 1
            elif pery[y][x] < 0.3:
                output[y][x] = 2
            elif pery[y][x] < 0.5:
                output[y][x] = 3
            else:
                output[y][x] = 4

    return output

def genmap(xsquare=9, ysquare=6, csv_flg=1, highmount=0.5, forest=0.3, land=-0.2,
           sand=-0.3, normalsea=-0.5, shahei_build=0.2, shogai_build=0.05, pixel=200):
    img = Image.open('input_start.png')

    tilepixel = 1
    squarepixel = int(pixel / tilepixel)
    fieldFlg = True
    img2 = Image.new("RGB", img.size, (255, 255, 255))
    img2.paste(img, mask=img.split()[3])
    draw = ImageDraw.Draw(img2)

    z = 0
    fieldtile_y = 0
    xpixel, ypixel = img.size
    #maxpixel = 0
    #if xpixel >= ypixel:
    #    maxpixel = xpixel
    #else:
    #    maxpixel = ypixel

    #canvas = Image.new("RGB", (xpixel, ypixel), "#FFFFFF")
    #draw = ImageDraw.Draw(canvas)
    outputText = ""

    #N = int(maxpixel / tilepixel)
    #pery = np.zeros((N, N))
    #for i in np.random.rand(1):  # パーリンノイズは周波数を変えて何枚か重ねると本領を発揮するらしいのでループして加算
    #    perx = np.linspace(0, 8 * i, N)
    #    print(perx.shape)
    #    r = np.array(np.meshgrid(perx, perx))
    #    print(r.shape)
    #    pery += perlin(r)  # meshgridの形(2,N,N)で渡す
        #print(pery[1])

    mount_col1 = "#B8860B"
    mount_col2 = "#8B4513"
    forest_col1 = "#006400"
    forest_col2 = "#228B22"
    land1_col1 = "#7CFC00"
    land1_col2 = "#00FF7F"
    sand_col1 = "#FFF8DC"
    sand_col2 = "#FFE4C4"
    sea_col1 = "#4169E1"
    sea_col2 = "#6495ED"
    deepsea_col1 = "#000080"
    deepsea_col2 = "#0000cd"
    build_col1 = "#d3d3d3"
    build_col2 = "#696969"
    space_col1 = "#000080"
    space_col2 = "#FFFF00"

    #ymaxtap = pery.shape
    #xmaxtap = pery[0].shape
    canvasxmax = int(xpixel / tilepixel)
    canvasymax = int(ypixel / tilepixel)
    ymax = int(canvasymax / pixel)
    xmax = int(canvasxmax / pixel)
    print(ymax)
    print(xmax)
    outputMapBigArray = np.zeros((canvasymax, canvasxmax))
    for y in range(ymax):
        for x in range(xmax):
            checkpixelx = int((x * pixel) + (pixel / 2))
            checkpixely = int((y * pixel) + (pixel / 2))
            rgb = img.getpixel((checkpixelx, checkpixely))
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            gray = int((r + g + b) / 3)
            if (gray <= 64):
                tile = pixelCreate.pixel_create(xmax=squarepixel, ymax=squarepixel, color1=space_col1, color2=space_col2,
                                               rate=0.01)
                img2.paste(tile, (x * squarepixel, y * squarepixel))
                build_num = random.randint(3, 5)
                for i in range(build_num):
                    buildsizemin = 13
                    buildsizemax = 39
                    buildposmin = buildsizemax
                    buildposmax = pixel - buildsizemax
                    buildsize = random.randint(buildsizemin, buildsizemax)
                    buildx = random.randint(buildposmin, buildposmax) + (x * pixel)
                    buildy = random.randint(buildposmin, buildposmax) + (y * pixel)
                    buildxstart = buildx - (buildsize / 2)
                    buildxend = buildx + (buildsize / 2)
                    buildystart = buildy - (buildsize / 2)
                    buildyend = buildy + (buildsize / 2)
                    draw.ellipse((buildxstart, buildystart, buildxend, buildyend), fill=mount_col1,
                                   outline=mount_col2)
                outputText = outputText + "■,"
            elif (gray <= 128):
                tile = pixelCreate.pixel_create(xmax=squarepixel, ymax=squarepixel, color1=space_col1, color2=space_col2,
                                                rate=0.01)
                img2.paste(tile, (x * squarepixel, y * squarepixel))
                build_num = random.randint(2, 5)
                for i in range(build_num):
                    buildsizemin = 10
                    buildsizemax = 30
                    buildposmin = buildsizemax
                    buildposmax = pixel - buildsizemax
                    buildsize = random.randint(buildsizemin, buildsizemax)
                    buildx = random.randint(buildposmin, buildposmax) + (x * pixel)
                    buildy = random.randint(buildposmin, buildposmax) + (y * pixel)
                    buildxstart = buildx - (buildsize / 2)
                    buildxend = buildx + (buildsize / 2)
                    buildystart = buildy - (buildsize / 2)
                    buildyend = buildy + (buildsize / 2)
                    draw.ellipse((buildxstart, buildystart, buildxend, buildyend), fill=mount_col1,
                                outline=mount_col2)
                outputText = outputText + "＃,"
            elif (gray <= 192):
                tile = pixelCreate.pixel_create(xmax=squarepixel, ymax=squarepixel, color1=space_col1, color2=space_col2,
                                                rate=0.01)
                img2.paste(tile, (x * squarepixel, y * squarepixel))
                build_num = random.randint(2, 5)
                for i in range(build_num):
                    buildsizemin = 7
                    buildsizemax = 21
                    buildposmin = buildsizemax
                    buildposmax = pixel - buildsizemax
                    buildsize = random.randint(buildsizemin, buildsizemax)
                    buildx = random.randint(buildposmin, buildposmax) + (x * pixel)
                    buildy = random.randint(buildposmin, buildposmax) + (y * pixel)
                    buildxstart = buildx - (buildsize / 2)
                    buildxend = buildx + (buildsize / 2)
                    buildystart = buildy - (buildsize / 2)
                    buildyend = buildy + (buildsize / 2)
                    draw.ellipse((buildxstart, buildystart, buildxend, buildyend), fill=mount_col1,
                                outline=mount_col2)
                outputText = outputText + "＝,"
            else:
                tile = pixelCreate.pixel_create(xmax=squarepixel, ymax=squarepixel, color1=space_col1, color2=space_col2,
                                                rate=0.01)
                img2.paste(tile, (x * squarepixel, y * squarepixel))
                outputText = outputText + "　,"
                #outputMapBigArray[y][x] = 2

        outputText = outputText[:-1] + "\n"
    outputText = outputText[:-1]

    f = open('output_map_csv.csv', 'w')
    f.write(outputText)
    f.close()

    #landseaout = landsea(pery)
    #plt.imshow(landseaout)
    #plt.show()

    #draw.point((i, j), color2)

    img2.save("output_map.png")

    return

if __name__ == '__main__':
    print("Program Start")
    genmap()
    print("Program End")