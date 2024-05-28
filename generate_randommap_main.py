import genmap11
from tkinter import *
import tkinter.messagebox as messagebox
import sys

xmax = 9
ymax = 6
pix = 200
sky = 100 #最上
highmount = 50 #以上は高山
forest = 30 #以上は森林
land = -20 #以上は平地
sand = -30 #以上は砂地
normalsea = -50 #以上は通常水地
deepsea = -100 #以上は深水
shahei_build = 4 #遮蔽建物の割合
shogai_build = 1 #障害建物の割合

def is_num(a):
    try:
        int(a)
    except:
        return False
    return True

def isfloat(s):  # 浮動小数点数値を表しているかどうかを判定
    try:
        float(s)  # 文字列を実際にfloat関数で変換してみる
    except ValueError:
        return False
    else:
        return True

def gen(text_x, text_y, csv_flg, text_highmount, text_forest, text_land, text_sand, text_normalsea
        , text_shahei_build, text_shogai_build, color="#FFFFFF"):
    genxmax = xmax
    errFlg = False
    if text_x.isdecimal() or text_x == "":
        genxmax = int(text_x)
    else:
        messagebox.showinfo('エラー', '「横スクウェア数」には数値を入力してください。')
        errFlg = True

    genymax = ymax
    if text_y.isdecimal() or text_y == "":
        genymax = int(text_y)
    else:
        messagebox.showinfo('エラー', '「縦スクウェア数」には数値を入力してください。')
        errFlg = True

    highmount = text_highmount
    if isfloat(highmount) or highmount == "":
        highmount = float(highmount) / 100
    else:
        messagebox.showinfo('エラー', '「高山ライン」には数値を入力してください。')
        errFlg = True

    forest = text_forest
    if isfloat(forest) or forest == "":
        forest = float(forest) / 100
    else:
        messagebox.showinfo('エラー', '「森林ライン」には数値を入力してください。')
        errFlg = True

    land = text_land
    if isfloat(land) or land == "":
        land = float(land) / 100
    else:
        messagebox.showinfo('エラー', '「平地ライン」には数値を入力してください。')
        errFlg = True

    sand = text_sand
    if isfloat(sand) or sand == "":
        sand = float(sand) / 100
    else:
        messagebox.showinfo('エラー', '「砂地ライン」には数値を入力してください。')
        errFlg = True

    normalsea = text_normalsea
    if isfloat(normalsea) or normalsea == "":
        normalsea = float(normalsea) / 100
    else:
        messagebox.showinfo('エラー', '「水地ライン」には数値を入力してください。')
        errFlg = True

    shahei_build = text_shahei_build
    if isfloat(shahei_build) or shahei_build == "":
        shahei_build = float(shahei_build) / 100
    else:
        messagebox.showinfo('エラー', '「遮蔽建物の割合」には数値を入力してください。')
        errFlg = True

    shogai_build = text_shogai_build
    if isfloat(shogai_build) or shogai_build == "":
        shogai_build = float(shogai_build) / 100
    else:
        messagebox.showinfo('エラー', '「障害建物の割合」には数値を入力してください。')
        errFlg = True

    if highmount < forest or forest < land or land < sand or sand < normalsea:
        messagebox.showinfo('エラー', 'ラインの数値の大小に誤りがあります')
        errFlg = True

    if shahei_build < shogai_build:
        messagebox.showinfo('エラー', '建物の数値の大小に誤りがあります')
        errFlg = True

    if not errFlg:
        genmap11.genmap(genxmax, genymax, csv_flg, highmount, forest, land, sand, normalsea, shahei_build, shogai_build)
        messagebox.showinfo('生成完了', '出力しました')

def setXmax(text_x):
    if text_x.isdecimal() or text_x == "":
        xmax = text_x
    else:
        messagebox.showinfo('エラー', '「横スクウェア数」には数値を入力してください。')


def setYmax(text_y):
    if text_y.isdecimal() or text_y == "":
        ymax = text_y
    else:
        messagebox.showinfo('エラー', '「縦スクウェア数」には数値を入力してください。')


def setPix(text_pix):
    if text_pix.isdecimal() or text_pix == "":
        pix = text_pix
    else:
        messagebox.showinfo('エラー', '「スクウェアピクセル数」には数値を入力してください。')


try:
    root = Tk()
    # ----------- ①Window作成 ----------- #
    root.title('ランダムマップ生成')  # 画面タイトル設定
    root.geometry('300x550')  # 画面サイズ設定
    root.resizable(False, False)  # リサイズ不可に設定

    # ----------- ②Frameを定義 ----------- #
    frame1 = Frame(root, width=150, height=50)  # Label
    frame2 = Frame(root, width=150, height=50)  # Button, Entry
    # frame3 = Frame(root, width=150, height=50)  # Checkbutton
    frame4 = Frame(root, width=150, height=50)  # Radiobutton
    frame5 = Frame(root, width=150, height=50)  # Spinbox
    # frame6 = Frame(root, width=150, height=50)  # Listbox
    frame7 = Frame(root, width=150, height=50)  # Canvas
    frame8 = Frame(root, width=150, height=50)  # Canvas用ボタン
    # frame9 = Frame(root, width=150, height=50)  # Photoimage
    frame10 = Frame(root, width=150, height=50)  # Canvas
    frame11 = Frame(root, width=150, height=50)  # Canvas用ボタン

    frame13 = Frame(root, width=150, height=50)  # Label
    frame14 = Frame(root, width=150, height=50)  # Button, Entry
    # frame3 = Frame(root, width=150, height=50)  # Checkbutton
    frame16 = Frame(root, width=150, height=50)  # Radiobutton
    frame17 = Frame(root, width=150, height=50)  # Spinbox
    # frame6 = Frame(root, width=150, height=50)  # Listbox
    frame19 = Frame(root, width=150, height=50)  # Canvas
    frame20 = Frame(root, width=150, height=50)  # Canvas用ボタン
    # frame9 = Frame(root, width=150, height=50)  # Photoimage
    frame22 = Frame(root, width=150, height=50)  # Canvas
    frame23 = Frame(root, width=150, height=50)  # Canvas用ボタン

    frame25 = Frame(root, width=150, height=50)  # Canvas
    frame26 = Frame(root, width=150, height=50)  # Canvas用ボタン

    frame28 = Frame(root, width=150, height=50)  # Canvas
    frame29 = Frame(root, width=150, height=50)  # Canvas用ボタン

    frame31 = Frame(root, width=150, height=50)  # Canvas
    frame32 = Frame(root, width=150, height=50)  # Canvas用ボタン

    # Frameサイズを固定
    frame1.propagate(False)
    frame2.propagate(False)
    # frame3.propagate(False)
    frame4.propagate(False)
    frame5.propagate(False)
    # frame6.propagate(False)
    frame7.propagate(False)
    frame8.propagate(False)
    # frame9.propagate(False)
    frame10.propagate(False)
    frame11.propagate(False)

    frame13.propagate(False)
    frame14.propagate(False)

    frame16.propagate(False)
    frame17.propagate(False)

    frame19.propagate(False)
    frame20.propagate(False)

    frame22.propagate(False)
    frame23.propagate(False)

    frame25.propagate(False)
    frame26.propagate(False)

    frame28.propagate(False)
    frame29.propagate(False)

    frame31.propagate(False)
    frame32.propagate(False)

    # Frameを配置（grid）
    frame1.grid(row=0, column=0)
    frame2.grid(row=0, column=1)
    # frame3.grid(row=0, column=2)
    frame4.grid(row=1, column=0)
    frame5.grid(row=1, column=1)
    # frame6.grid(row=1, column=2)
    frame7.grid(row=2, column=0)
    frame8.grid(row=2, column=1)
    # frame9.grid(row=2, column=2)
    frame10.grid(row=3, column=0)
    frame11.grid(row=3, column=1)

    frame13.grid(row=4, column=0)
    frame14.grid(row=4, column=1)

    frame16.grid(row=5, column=0)
    frame17.grid(row=5, column=1)

    frame19.grid(row=6, column=0)
    frame20.grid(row=6, column=1)

    frame22.grid(row=7, column=0)
    frame23.grid(row=7, column=1)

    frame25.grid(row=8, column=0)
    frame26.grid(row=8, column=1)

    frame28.grid(row=9, column=0)
    frame29.grid(row=9, column=1)

    frame31.grid(row=10, column=0)
    frame32.grid(row=10, column=1)

    label_1a = Label(frame1, text='横スクウェア数', font=('System', 14))
    label_1a.pack()

    # == Entry(Frame2) == #
    entry_2b = Entry(frame2, width=14)
    entry_2b.insert(0, str(xmax))
    text_x = StringVar()
    button_2b = Button(frame2, text='反映',
                       command=lambda: [text_x.set(entry_2b.get()), setXmax(entry_2b.get())])
    label_2b = Label(frame2, textvariable=text_x, font=('System', 14))

    entry_2b.pack()
    # button_2b.pack()
    # label_2b.pack()

    label_4a = Label(frame4, text='縦スクウェア数', font=('System', 14))
    label_4a.pack()

    # == Entry(Frame5) == #
    entry_5b = Entry(frame5, width=14)
    entry_5b.insert(0, str(ymax))
    text_y = StringVar()
    button_5b = Button(frame5, text='反映',
                       command=lambda: [text_y.set(entry_5b.get()), setYmax(entry_5b.get())])
    label_5b = Label(frame5, textvariable=text_y, font=('System', 14))

    entry_5b.pack()
    # button_5b.pack()
    # label_5b.pack()

    label_7a = Label(frame7, text='高山ライン', font=('System', 14))
    label_7a.pack()

    # == Entry(frame8) == #
    entry_8b = Entry(frame8, width=14)
    entry_8b.insert(0, str(highmount))
    text_hignmount = StringVar()
    button_8b = Button(frame8, text='反映',
                       command=lambda: [text_hignmount.set(entry_8b.get()), setYmax(entry_8b.get())])
    label_8b = Label(frame8, textvariable=text_hignmount, font=('System', 14))

    entry_8b.pack()

    label_10a = Label(frame10, text='森林ライン', font=('System', 14))
    label_10a.pack()

    # == Entry(frame11) == #
    entry_11b = Entry(frame11, width=14)
    entry_11b.insert(0, str(forest))
    text_forest = StringVar()
    button_11b = Button(frame11, text='反映',
                       command=lambda: [text_forest.set(entry_11b.get()), setYmax(entry_11b.get())])
    label_11b = Label(frame11, textvariable=text_forest, font=('System', 14))

    entry_11b.pack()

    label_13a = Label(frame13, text='平地ライン', font=('System', 14))
    label_13a.pack()

    # == Entry(frame14) == #
    entry_14b = Entry(frame14, width=14)
    entry_14b.insert(0, str(land))
    text_land = StringVar()
    button_14b = Button(frame14, text='反映',
                        command=lambda: [text_land.set(entry_14b.get()), setYmax(entry_14b.get())])
    label_14b = Label(frame14, textvariable=text_land, font=('System', 14))

    entry_14b.pack()

    label_16a = Label(frame16, text='砂地ライン', font=('System', 14))
    label_16a.pack()

    # == Entry(frame17) == #
    entry_17b = Entry(frame17, width=14)
    entry_17b.insert(0, str(sand))
    text_sand = StringVar()
    button_17b = Button(frame17, text='反映',
                        command=lambda: [text_sand.set(entry_17b.get()), setYmax(entry_17b.get())])
    label_17b = Label(frame17, textvariable=text_sand, font=('System', 14))

    entry_17b.pack()

    label_19a = Label(frame19, text='水地ライン', font=('System', 14))
    label_19a.pack()

    # == Entry(frame20) == #
    entry_20b = Entry(frame20, width=14)
    entry_20b.insert(0, str(normalsea))
    text_normalsea = StringVar()
    button_20b = Button(frame20, text='反映',
                        command=lambda: [text_normalsea.set(entry_20b.get()), setYmax(entry_20b.get())])
    label_20b = Label(frame20, textvariable=text_normalsea, font=('System', 14))

    entry_20b.pack()

    label_22a = Label(frame22, text='遮蔽建物の割合', font=('System', 14))
    label_22a.pack()

    # == Entry(frame23) == #
    entry_23b = Entry(frame23, width=14)
    entry_23b.insert(0, str(shahei_build))
    text_shahei_build = StringVar()
    button_23b = Button(frame23, text='反映',
                        command=lambda: [text_shahei_build.set(entry_23b.get()), setYmax(entry_23b.get())])
    label_23b = Label(frame23, textvariable=text_shahei_build, font=('System', 14))

    entry_23b.pack()

    label_25a = Label(frame25, text='障害建物の割合', font=('System', 14))
    label_25a.pack()

    # == Entry(frame26) == #
    entry_26b = Entry(frame26, width=14)
    entry_26b.insert(0, str(shogai_build))
    text_shogai_build = StringVar()
    button_26b = Button(frame26, text='反映',
                        command=lambda: [text_shogai_build.set(entry_26b.get()), setYmax(entry_26b.get())])
    label_26b = Label(frame26, textvariable=text_shogai_build, font=('System', 14))

    entry_26b.pack()

    label_28a = Label(frame28, text='地形の表示', font=('System', 14))
    label_28a.pack()

    # == Entry(Frame8) == #
    # entry_8b = Entry(frame8, width=17)
    # entry_8b.pack()

    # チェック有無変数
    var = IntVar()

    # value=0のラジオボタンにチェックを入れる
    var.set(1)

    # ラジオボタン作成
    rdo1 = Radiobutton(frame29, value=1, variable=var, text='あり')
    rdo1.pack()

    rdo2 = Radiobutton(frame29, value=0, variable=var, text='なし')
    rdo2.pack()

    button_31a = Button(frame31, text='生成', command=lambda: [gen(entry_2b.get(), entry_5b.get(), var.get(),
                                                                   entry_8b.get(), entry_11b.get(), entry_14b.get(),
                                                                   entry_17b.get(), entry_20b.get(), entry_23b.get(),
                                                                   entry_26b.get())])
    button_31a.pack(padx=5, pady=10, expand=True)

    button_32a = Button(frame32, text='終了', command=lambda: sys.exit())
    button_32a.pack(padx=5, pady=10, expand=True)
    #コードをここに書くと発生する例外がファイルに出力される。
    root.mainloop()
except Exception as e:
    import traceback
    with open('error.log', 'a') as f:
        traceback.print_exc( file=f)