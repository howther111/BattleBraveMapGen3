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

def genmap(xsquare=9, ysquare=6, csv_flg=1, pixel=200):
    tilepixel = 8
    squarepixel = int(pixel / tilepixel)
    fieldFlg = True

    z = 0
    fieldtile_y = 0
    xpixel = xsquare * pixel
    ypixel = ysquare * pixel
    maxpixel = 0
    if xpixel >= ypixel:
        maxpixel = xpixel
    else:
        maxpixel = ypixel

    canvas = Image.new("RGB", (xpixel, ypixel), "#FFFFFF")
    draw = ImageDraw.Draw(canvas)
    outputText = ""

    N = int(maxpixel / tilepixel)
    pery = np.zeros((N, N))
    for i in np.random.rand(1):  # パーリンノイズは周波数を変えて何枚か重ねると本領を発揮するらしいのでループして加算
        perx = np.linspace(0, 8 * i, N)
        print(perx.shape)
        r = np.array(np.meshgrid(perx, perx))
        print(r.shape)
        pery += perlin(r)  # meshgridの形(2,N,N)で渡す
        #print(pery[1])

    mount_col1 = "#8B4513"
    mount_col2 = "#B8860B"
    forest_col1 = "#006400"
    forest_col2 = "#228B22"
    land1_col1 = "#98FB98"
    land1_col2 = "#00FF7F"
    sand_col1 = "#FFF8DC"
    sand_col2 = "#FFE4C4"
    sea_col1 = "#4169E1"
    sea_col2 = "#6495ED"

    ymaxtap = pery.shape
    xmaxtap = pery[0].shape
    canvasxmax = int(xpixel / tilepixel)
    canvasymax = int(ypixel / tilepixel)
    ymax = ymaxtap[0]
    xmax = xmaxtap[0]
    print(ymax)
    print(xmax)
    outputMapBigArray = np.zeros((canvasymax, canvasxmax))
    for y in range(canvasymax):
        for x in range(canvasxmax):
            if pery[y][x] < -0.3:
                tile = pixelCreate.pixel_create(xmax=tilepixel, ymax=tilepixel, color1=sea_col1, color2=sea_col2,
                                                rate=0.2)
                canvas.paste(tile, (x * tilepixel, y * tilepixel))
                outputText = outputText + "水,"
                outputMapBigArray[y][x] = -1
            elif pery[y][x] < -0.2:
                tile = pixelCreate.pixel_create(xmax=tilepixel, ymax=tilepixel, color1=sand_col1, color2=sand_col2,
                                                rate=0.2)
                canvas.paste(tile, (x * tilepixel, y * tilepixel))
                outputText = outputText + "　,"
            elif pery[y][x] < 0.3:
                tile = pixelCreate.pixel_create(xmax=tilepixel, ymax=tilepixel, color1=land1_col1, color2=land1_col2,
                                                rate=0.2)
                canvas.paste(tile, (x * tilepixel, y * tilepixel))
                outputText = outputText + "　,"
            elif pery[y][x] < 0.5:
                tile = pixelCreate.pixel_create(xmax=tilepixel, ymax=tilepixel, color1=forest_col1, color2=forest_col2,
                                                rate=0.2)
                canvas.paste(tile, (x * tilepixel, y * tilepixel))
                outputText = outputText + "▼,"
                outputMapBigArray[y][x] = 1
            else:
                tile = pixelCreate.pixel_create(xmax=tilepixel, ymax=tilepixel, color1=mount_col1, color2=mount_col2,
                                                rate=0.2)
                canvas.paste(tile, (x * tilepixel, y * tilepixel))
                outputText = outputText + "▲,"
                outputMapBigArray[y][x] = 2

        outputText = outputText[:-1] + "\n"
    outputText = outputText[:-1]

    outputMapArray = np.zeros((ysquare, xsquare))
    outputMinText = ""
    waterBorder = ((squarepixel ** 2) - (int((squarepixel ** 2) / 1.5))) * -1
    forestBorder = ((squarepixel ** 2) - (int((squarepixel ** 2) / 1.5))) * 1
    mountBorder = ((squarepixel ** 2) - (int((squarepixel ** 2) / 1.5))) * 2.5
    for y in range(ysquare):
        for x in range(xsquare):
            meansquare = np.zeros((squarepixel, squarepixel))
            meanNum = 0
            for y_square in range(squarepixel):
                for x_square in range(squarepixel):
                    x_coor = x * squarepixel + x_square
                    y_coor = y * squarepixel + y_square
                    meanNum = meanNum + outputMapBigArray[y_coor][x_coor]
            if meanNum < waterBorder:
                outputMapArray[y][x] = -1
                if csv_flg == 1:
                    outputMinText = outputMinText + "　,"
                elif csv_flg == 0:
                    outputMinText = outputMinText + "　,"
            elif meanNum > forestBorder and meanNum <= mountBorder:
                outputMapArray[y][x] = 1
                if csv_flg == 1:
                    outputMinText = outputMinText + "■,"
                elif csv_flg == 0:
                    outputMinText = outputMinText + "　,"
            elif meanNum > mountBorder:
                outputMapArray[y][x] = 2
                if csv_flg == 1:
                    outputMinText = outputMinText + "■,"
                elif csv_flg == 0:
                    outputMinText = outputMinText + "　,"

            else:
                outputMapArray[y][x] = 0
                outputMinText = outputMinText + "　,"

        outputMinText = outputMinText[:-1] + "\n"
    outputMinText = outputMinText[:-1]

    mapOutputText = ""


    #canvas.show()

    #f = open('output_map.txt', 'w')
    #f.write(outputText)
    #f.close()

    f = open('output_map_csv.csv', 'w')
    f.write(outputMinText)
    f.close()

    #landseaout = landsea(pery)
    #plt.imshow(landseaout)
    #plt.show()

    #draw.point((i, j), color2)

    canvas.save("output_map.png")

    return