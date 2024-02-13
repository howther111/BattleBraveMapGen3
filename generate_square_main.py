from tkinter import *
import tkinter.messagebox as messagebox
#from generateMap import *
from generateMapFunc import *

xmax = 9
ymax = 6
pix = 200
def gen(text_x, text_y, color="#FFFFFF"):
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

    if not errFlg:
        generateMapFunc(genxmax, genymax, color)


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

root = Tk()
# ----------- ①Window作成 ----------- #
root.title('スクウェアマップ生成')   # 画面タイトル設定
root.geometry('300x200')        # 画面サイズ設定
root.resizable(False, False)    # リサイズ不可に設定

# ----------- ②Frameを定義 ----------- #
frame1 = Frame(root, width=150, height=50)  # Label
frame2 = Frame(root, width=150, height=50)  # Button, Entry
#frame3 = Frame(root, width=150, height=50)  # Checkbutton
frame4 = Frame(root, width=150, height=50)  # Radiobutton
frame5 = Frame(root, width=150, height=50)  # Spinbox
#frame6 = Frame(root, width=150, height=50)  # Listbox
frame7 = Frame(root, width=150, height=50)  # Canvas
frame8 = Frame(root, width=150, height=50)  # Canvas用ボタン
#frame9 = Frame(root, width=150, height=50)  # Photoimage
frame10 = Frame(root, width=150, height=50)  # Canvas
frame11 = Frame(root, width=150, height=50)  # Canvas用ボタン

# Frameサイズを固定
frame1.propagate(False)
frame2.propagate(False)
#frame3.propagate(False)
frame4.propagate(False)
frame5.propagate(False)
#frame6.propagate(False)
frame7.propagate(False)
frame8.propagate(False)
#frame9.propagate(False)
frame10.propagate(False)
frame11.propagate(False)

# Frameを配置（grid）
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
#frame3.grid(row=0, column=2)
frame4.grid(row=1, column=0)
frame5.grid(row=1, column=1)
#frame6.grid(row=1, column=2)
frame7.grid(row=2, column=0)
frame8.grid(row=2, column=1)
#frame9.grid(row=2, column=2)
frame10.grid(row=3, column=0)
frame11.grid(row=3, column=1)

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
#button_2b.pack()
#label_2b.pack()

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
#button_5b.pack()
#label_5b.pack()

"""
label_7a = Label(frame7, text='スクウェアピクセル数', font=('System', 17))
label_7a.pack()

# == Entry(Frame8) == #
entry_8b = Entry(frame8, width=17)
entry_8b.insert(0, str(pix))
text_pix = StringVar()
button_8b = Button(frame8, text='反映',
            command=lambda: [text_pix.set(entry_8b.get()), setPix(entry_8b.get())])
label_8b = Label(frame8, textvariable=text_pix, font=('System', 17))

entry_8b.pack()
button_8b.pack()
label_8b.pack()
"""

label_7a = Label(frame7, text='カラー', font=('System', 14))
label_7a.pack()

# == Entry(Frame5) == #
entry_8b = Entry(frame8, width=14)
entry_8b.insert(0, "#000000")
col = StringVar()

entry_8b.pack()

button_10a = Button(frame10, text='生成', command=lambda: [gen(entry_2b.get(), entry_5b.get(), entry_8b.get())])
button_10a.pack(padx=5, pady=10, expand=True)

button_11a = Button(frame11, text='終了', command=exit)
button_11a.pack(padx=5, pady=10, expand=True)

root.mainloop()