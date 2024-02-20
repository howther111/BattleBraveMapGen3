from tkinter import *
import tkinter.messagebox as messagebox
import startPos
import sys

start_xpos = 1
start_ypos = 1
start_xwidth = 2
start_ywidth = 2
escape_xpos = 1
escape_ypos = 1
escape_xwidth = 1
escape_ywidth = 1

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

def editStart(text_start_xpos, text_start_ypos, text_start_xwidth, text_start_ywidth,
              text_escape_xpos, text_escape_ypos, text_escape_xwidth, text_escape_ywidth):
    errFlg = False
    start_xpos = text_start_xpos
    if text_start_xpos.isdecimal() or text_start_xpos == "":
        start_xpos = int(text_start_xpos)
    else:
        messagebox.showinfo('エラー', '「初期配置横開始地点」には数値を入力してください。')
        errFlg = True

    start_ypos = text_start_ypos
    if text_start_ypos.isdecimal() or text_start_ypos == "":
        start_ypos = int(text_start_ypos)
    else:
        messagebox.showinfo('エラー', '「初期配置縦開始地点」には数値を入力してください。')
        errFlg = True

    start_xwidth = text_start_xwidth
    if text_start_xwidth.isdecimal() or text_start_xwidth == "":
        start_xwidth = int(text_start_xwidth)
    else:
        messagebox.showinfo('エラー', '「初期配置横幅」には数値を入力してください。')
        errFlg = True

    start_ywidth = text_start_ywidth
    if text_start_ywidth.isdecimal() or text_start_ywidth == "":
        start_ywidth = int(text_start_ywidth)
    else:
        messagebox.showinfo('エラー', '「初期配置縦幅」には数値を入力してください。')
        errFlg = True

    escape_xpos = text_escape_xpos
    if text_escape_xpos.isdecimal() or text_escape_xpos == "":
        escape_xpos = int(text_escape_xpos)
    else:
        messagebox.showinfo('エラー', '「逃走横開始地点」には数値を入力してください。')
        errFlg = True

    escape_ypos = text_escape_ypos
    if text_escape_ypos.isdecimal() or text_escape_ypos == "":
        escape_ypos = int(text_escape_ypos)
    else:
        messagebox.showinfo('エラー', '「逃走縦開始地点」には数値を入力してください。')
        errFlg = True

    escape_xwidth = text_escape_xwidth
    if text_escape_xwidth.isdecimal() or text_escape_xwidth == "":
        escape_xwidth = int(text_escape_xwidth)
    else:
        messagebox.showinfo('エラー', '「逃走横幅」には数値を入力してください。')
        errFlg = True

    escape_ywidth = text_escape_ywidth
    if text_escape_ywidth.isdecimal() or text_escape_ywidth == "":
        escape_ywidth = int(text_escape_ywidth)
    else:
        messagebox.showinfo('エラー', '「逃走縦幅」には数値を入力してください。')
        errFlg = True

    if not errFlg:
        startPos.edit(start_xpos, start_ypos, start_xwidth, start_ywidth,
                      escape_xpos, escape_ypos, escape_xwidth, escape_ywidth)
        messagebox.showinfo('生成完了', '出力しました')

if __name__ == "__main__":
    print("EditStart")
    try:
        root = Tk()
        # ----------- ①Window作成 ----------- #
        root.title('初期配置設定')  # 画面タイトル設定
        root.geometry('300x450')  # 画面サイズ設定
        root.resizable(False, False)  # リサイズ不可に設定

        # ----------- ②Frameを定義 ----------- #
        frame1 = Frame(root, width=150, height=50)  # Label
        frame2 = Frame(root, width=150, height=50)  # Button, Entry

        frame4 = Frame(root, width=150, height=50)  # Radiobutton
        frame5 = Frame(root, width=150, height=50)  # Spinbox

        frame7 = Frame(root, width=150, height=50)  # Canvas
        frame8 = Frame(root, width=150, height=50)  # Canvas用ボタン

        frame10 = Frame(root, width=150, height=50)  # Canvas
        frame11 = Frame(root, width=150, height=50)  # Canvas用ボタン

        frame13 = Frame(root, width=150, height=50)  # Label
        frame14 = Frame(root, width=150, height=50)  # Button, Entry

        frame16 = Frame(root, width=150, height=50)  # Radiobutton
        frame17 = Frame(root, width=150, height=50)  # Spinbox

        frame19 = Frame(root, width=150, height=50)  # Canvas
        frame20 = Frame(root, width=150, height=50)  # Canvas用ボタン

        frame22 = Frame(root, width=150, height=50)  # Canvas
        frame23 = Frame(root, width=150, height=50)  # Canvas用ボタン

        frame25 = Frame(root, width=150, height=50)  # Canvas
        frame26 = Frame(root, width=150, height=50)  # Canvas用ボタン

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

        label_1a = Label(frame1, text='初期配置\n横開始地点', font=('System', 14))
        label_1a.pack()

        # == Entry(Frame2) == #
        entry_2b = Entry(frame2, width=14)
        entry_2b.insert(0, str(start_xpos))
        text_start_xpos = StringVar()
        button_2b = Button(frame2, text='反映',
                           command=lambda: [text_start_xpos.set(entry_2b.get())])
        label_2b = Label(frame2, textvariable=text_start_xpos, font=('System', 14))

        entry_2b.pack()

        label_4a = Label(frame4, text='初期配置\n縦開始地点', font=('System', 14))
        label_4a.pack()

        # == Entry(Frame5) == #
        entry_5b = Entry(frame5, width=14)
        entry_5b.insert(0, str(start_ypos))
        text_start_ypos = StringVar()
        button_5b = Button(frame5, text='反映',
                           command=lambda: [text_start_ypos.set(entry_5b.get())])
        label_5b = Label(frame5, textvariable=text_start_ypos, font=('System', 14))

        entry_5b.pack()
        # button_5b.pack()
        # label_5b.pack()

        label_7a = Label(frame7, text='初期配置\n横幅', font=('System', 14))
        label_7a.pack()

        # == Entry(frame8) == #
        entry_8b = Entry(frame8, width=14)
        entry_8b.insert(0, str(start_xwidth))
        text_start_xwidth = StringVar()
        button_8b = Button(frame8, text='反映',
                           command=lambda: [text_start_xwidth.set(entry_8b.get())])
        label_8b = Label(frame8, textvariable=text_start_xwidth, font=('System', 14))

        entry_8b.pack()

        label_10a = Label(frame10, text='初期配置\n縦幅', font=('System', 14))
        label_10a.pack()

        # == Entry(frame11) == #
        entry_11b = Entry(frame11, width=14)
        entry_11b.insert(0, str(start_ywidth))
        text_start_ywidth = StringVar()
        button_11b = Button(frame11, text='反映',
                            command=lambda: [text_start_ywidth.set(entry_11b.get())])
        label_11b = Label(frame11, textvariable=text_start_ywidth, font=('System', 14))

        entry_11b.pack()

        label_13a = Label(frame13, text='逃走\n横開始地点', font=('System', 14))
        label_13a.pack()

        # == Entry(frame14) == #
        entry_14b = Entry(frame14, width=14)
        entry_14b.insert(0, str(escape_xpos))
        text_escape_xpos = StringVar()
        button_14b = Button(frame14, text='反映',
                            command=lambda: [text_escape_xpos.set(entry_14b.get())])
        label_14b = Label(frame14, textvariable=text_escape_xpos, font=('System', 14))

        entry_14b.pack()

        label_16a = Label(frame16, text='逃走\n縦開始地点', font=('System', 14))
        label_16a.pack()

        # == Entry(frame17) == #
        entry_17b = Entry(frame17, width=14)
        entry_17b.insert(0, str(escape_ypos))
        text_escape_ypos = StringVar()
        button_17b = Button(frame17, text='反映',
                            command=lambda: [text_escape_ypos.set(entry_17b.get())])
        label_17b = Label(frame17, textvariable=text_escape_ypos, font=('System', 14))

        entry_17b.pack()

        label_19a = Label(frame19, text='逃走\n横幅', font=('System', 14))
        label_19a.pack()

        # == Entry(frame20) == #
        entry_20b = Entry(frame20, width=14)
        entry_20b.insert(0, str(escape_xwidth))
        text_escape_xwidth = StringVar()
        button_20b = Button(frame20, text='反映',
                            command=lambda: [text_escape_xwidth.set(entry_20b.get())])
        label_20b = Label(frame20, textvariable=text_escape_xwidth, font=('System', 14))

        entry_20b.pack()

        label_22a = Label(frame22, text='逃走\n縦幅', font=('System', 14))
        label_22a.pack()

        # == Entry(frame23) == #
        entry_23b = Entry(frame23, width=14)
        entry_23b.insert(0, str(escape_ywidth))
        text_escape_ywidth = StringVar()
        button_23b = Button(frame23, text='反映',
                            command=lambda: [text_escape_ywidth.set(entry_23b.get())])
        label_23b = Label(frame23, textvariable=text_escape_ywidth, font=('System', 14))

        entry_23b.pack()

        button_25a = Button(frame25, text='生成', command=lambda: [editStart(entry_2b.get(), entry_5b.get(),
                                                                             entry_8b.get(), entry_11b.get(),
                                                                             entry_14b.get(),
                                                                             entry_17b.get(), entry_20b.get(),
                                                                             entry_23b.get())])
        button_25a.pack(padx=5, pady=10, expand=True)

        button_26a = Button(frame26, text='終了', command=lambda: sys.exit())
        button_26a.pack(padx=5, pady=10, expand=True)

        root.mainloop()

    except Exception as e:
        import traceback

        with open('error.log', 'a') as f:
            traceback.print_exc(file=f)