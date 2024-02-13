import pyxel

TM = 0
IMGBANK = 1

class Stage:

    def __init__(self,width,height) -> None:
        self.width = width * 8
        self.height = height * 8
        self.disp_w = width
        self.disp_h = height
        self.scroll_x = 0
        self.scroll_y = 0
        self.col = 0
        return

    def genmap(self,num):
        z = 0
        fieldtile_y = 0
        for y in range(self.width//8):
            for x in range(self.height//8):
                n = 0
                scale = 0.035
                amp = 1
                for i in range(num):
                    n += pyxel.noise(x*scale, y*scale, z*scale) * amp
                    scale *= 2
                    amp *= 0.5
                    
                if n < -0.3:
                    tileNo = 1
                elif n < -0.2:
                    tileNo = 2
                elif n < 0.3:
                    tileNo = 3
                else:
                    tileNo = 4
                pyxel.tilemap(TM).pset(x,y,(tileNo,fieldtile_y))

        return

    def update(self,x,y):
        self.scroll_x = 0
        self.scroll_y = 0
        return

    def draw(self):
        pyxel.camera()
        pyxel.bltm(0,0, TM, self.scroll_x,self.scroll_y, self.disp_w,self.disp_h, self.col)
        pyxel.camera(self.scroll_x,self.scroll_y)
        return

def genmappyxel(xmax, ymax):
    CAP = 2
    PIX = int(200 / CAP)
    APP_WIDTH = (xmax * PIX) + PIX
    APP_HEIGHT = (ymax * PIX) + PIX
    pyxel.init(APP_WIDTH, APP_HEIGHT, title="Alt+1キーを押下後、Escキーを押下して終了してください。", capture_scale=CAP)

    data = ["00000000cccc6cccffffffffbbbbbbbb33333333000000000000000000000000",
            "000000006cccccccfbffffffb3bbb3bbb333333b000000000000000000000000",
            "00000000cc6cccc6fffbffffbbbbbbbb33b333b3000000000000000000000000",
            "00000000ccccccccfffffffbbbbb3bbb33333333000000000000000000000000",
            "00000000cccccc6cffffffff3bbbbbbb3333b333000000000000000000000000",
            "00000000ccc6ccccfbfffbffbbbbbbbb3333333b000000000000000000000000",
            "00000000ccccccccffffffffbb3bb3bb3b333333000000000000000000000000",
            "00000000c6ccccccfffbffffbbbbbbb33333b3b3000000000000000000000000", ]

    pyxel.image(IMGBANK).set(0, 0, data)
    pyxel.tilemap(TM).refimg = IMGBANK

    x = y = 0
    stg = Stage(APP_WIDTH, APP_HEIGHT)
    cnt = 3
    stg.genmap(cnt)

    pyxel.cls(0)
    #stg.draw()
    pyxel.camera()

    def update():
        stg.update(x=0, y=0)
        return

    def draw():
        stg.draw()
        return

    pyxel.run(update=update, draw=draw)

