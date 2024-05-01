from tkinter import *
import tkinter.messagebox as messagebox
import textPos
import sys

text_xpos = 1
text_ypos = 1
text_xwidth = 1
text_ywidth = 1
input_text_default = ""

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

def editStart(text_text_xpos, text_text_ypos, text_text_xwidth, text_text_ywidth,
              text_input_text):
    errFlg = False
    text_xpos = text_text_xpos
    if text_text_xpos.isdecimal() or text_text_xpos == "":
        text_xpos = int(text_text_xpos)
    else:
        messagebox.showinfo('エラー', '「指定横開始地点」には数値を入力してください。')
        errFlg = True

    text_ypos = text_text_ypos
    if text_text_ypos.isdecimal() or text_text_ypos == "":
        text_ypos = int(text_text_ypos)
    else:
        messagebox.showinfo('エラー', '「指定縦開始地点」には数値を入力してください。')
        errFlg = True

    text_xwidth = text_text_xwidth
    if text_text_xwidth.isdecimal() or text_text_xwidth == "":
        text_xwidth = int(text_text_xwidth)
    else:
        messagebox.showinfo('エラー', '「初期配置横幅」には数値を入力してください。')
        errFlg = True

    text_ywidth = text_text_ywidth
    if text_text_ywidth.isdecimal() or text_text_ywidth == "":
        text_ywidth = int(text_text_ywidth)
    else:
        messagebox.showinfo('エラー', '「初期配置縦幅」には数値を入力してください。')
        errFlg = True

    input_text = text_input_text

    if not errFlg:
        textPos.edit(text_xpos, text_ypos, text_xwidth, text_ywidth,
                      input_text)
        messagebox.showinfo('生成完了', '出力しました')

if __name__ == "__main__":
    print("EditStart")
    try:
        root = Tk()
        # ----------- ①Window作成 ----------- #
        root.title('初期配置設定')  # 画面タイトル設定
        root.geometry('300x300')  # 画面サイズ設定
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

        label_1a = Label(frame1, text='テキスト\n横開始地点', font=('System', 14))
        label_1a.pack()

        # == Entry(Frame2) == #
        entry_2b = Entry(frame2, width=14)
        entry_2b.insert(0, str(text_xpos))
        text_text_xpos = StringVar()
        button_2b = Button(frame2, text='反映',
                           command=lambda: [text_text_xpos.set(entry_2b.get())])
        label_2b = Label(frame2, textvariable=text_text_xpos, font=('System', 14))

        entry_2b.pack()

        label_4a = Label(frame4, text='テキスト\n縦開始地点', font=('System', 14))
        label_4a.pack()

        # == Entry(Frame5) == #
        entry_5b = Entry(frame5, width=14)
        entry_5b.insert(0, str(text_ypos))
        text_text_ypos = StringVar()
        button_5b = Button(frame5, text='反映',
                           command=lambda: [text_text_ypos.set(entry_5b.get())])
        label_5b = Label(frame5, textvariable=text_text_ypos, font=('System', 14))

        entry_5b.pack()
        # button_5b.pack()
        # label_5b.pack()

        label_7a = Label(frame7, text='テキスト\n横幅', font=('System', 14))
        label_7a.pack()

        # == Entry(frame8) == #
        entry_8b = Entry(frame8, width=14)
        entry_8b.insert(0, str(text_xwidth))
        text_text_xwidth = StringVar()
        button_8b = Button(frame8, text='反映',
                           command=lambda: [text_text_xwidth.set(entry_8b.get())])
        label_8b = Label(frame8, textvariable=text_text_xwidth, font=('System', 14))

        entry_8b.pack()

        label_10a = Label(frame10, text='テキスト\n縦幅', font=('System', 14))
        label_10a.pack()

        # == Entry(frame11) == #
        entry_11b = Entry(frame11, width=14)
        entry_11b.insert(0, str(text_ywidth))
        text_text_ywidth = StringVar()
        button_11b = Button(frame11, text='反映',
                            command=lambda: [text_text_ywidth.set(entry_11b.get())])
        label_11b = Label(frame11, textvariable=text_text_ywidth, font=('System', 14))

        entry_11b.pack()

        label_13a = Label(frame13, text="テキスト\n（1文字）", font=('System', 14))
        label_13a.pack()

        # == Entry(frame14) == #
        entry_14b = Entry(frame14, width=14)
        entry_14b.insert(0, str(input_text_default))
        input_text = StringVar()
        button_14b = Button(frame14, text='反映',
                            command=lambda: [input_text.set(entry_14b.get())])
        label_14b = Label(frame14, textvariable=input_text, font=('System', 14))

        entry_14b.pack()

        button_16a = Button(frame16, text='生成', command=lambda: [editStart(entry_2b.get(), entry_5b.get(),
                                                                             entry_8b.get(), entry_11b.get(),
                                                                             entry_14b.get())])
        button_16a.pack(padx=5, pady=10, expand=True)

        button_17a = Button(frame17, text='終了', command=lambda: sys.exit())
        button_17a.pack(padx=5, pady=10, expand=True)

        root.mainloop()

    except Exception as e:
        import traceback

        with open('error.log', 'a') as f:
            traceback.print_exc(file=f)