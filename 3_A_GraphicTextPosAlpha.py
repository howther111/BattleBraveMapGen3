import tkinter.ttk
from tkinter import *
import tkinter.messagebox as messagebox
import textPos
import sys
import metaga_mapchip_list
import csv
import numToAlpha

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


class Program:
    canvas = None
    root = None

    def __init__(self):
        print("EditStart")

        try:
            with open('input_map_csv.csv') as f:
                reader = csv.reader(f)
                l = [row for row in reader]

                lastsplitrow = ""
                print("\n-map start-\n")
                startrow = "  |"
                columnnum = 0
                for text in l[0]:
                    columnnum = columnnum + 1
                    columnnumtext = str(columnnum).zfill(2)
                    startrow = startrow + columnnumtext + "|"
                startrow = startrow + "  "
                print(startrow)

                rownum = 0

                for row in l:
                    rownum = rownum + 1
                    rownumtext = str(rownum).zfill(2)
                    newrow = rownumtext + "|"
                    charnum = 0
                    for char in row:
                        char.replace("\u3000", "  ")
                        newrow = newrow + char + "|"
                        charnum = charnum + 1

                    charnum = charnum

                    splitrow = "---"
                    for i in range(charnum):
                        splitrow = splitrow + "---"
                    splitrow = splitrow
                    lastsplitrow = splitrow

                    print(splitrow)
                    print(newrow)

                print(lastsplitrow)

                print("\n-map end-\n")

                outputcsv = l
        except:
            print("file read error")

        root = Tk()
        canvas1 = tkinter.Toplevel(root)  # ← Tk() の代わりに Toplevel を使う
        # ----------- ①Window作成 ----------- #
        root.title('テキストパレット')  # 画面タイトル設定
        root.geometry('300x100')  # 画面サイズ設定
        root.resizable(False, False)  # リサイズ不可に設定

        # ----------- ②Frameを定義 ----------- #
        frame1 = Frame(root, width=150, height=50)  # Label
        frame2 = Frame(root, width=150, height=50)  # Button, Entry

        frame4 = Frame(root, width=150, height=50)  # Radiobutton
        frame5 = Frame(root, width=150, height=50)  # Spinbox

        # Frameサイズを固定
        frame1.propagate(False)
        frame2.propagate(False)
        # frame3.propagate(False)
        frame4.propagate(False)
        frame5.propagate(False)
        # frame6.propagate(False)

        # Frameを配置（grid）
        frame1.grid(row=0, column=0)
        frame2.grid(row=0, column=1)
        # frame3.grid(row=0, column=2)
        frame4.grid(row=1, column=0)
        frame5.grid(row=1, column=1)

        label_13a = Label(frame1, text="テキスト", font=('System', 14))
        label_13a.pack()

        # == Entry(frame14) == #
        mapchip_list = metaga_mapchip_list.mapchip_list
        combobox_14b = tkinter.ttk.Combobox(frame2, font=('System', 14), values=mapchip_list, justify="center",
                                            width=14)
        # entry_14b = Entry(frame14, width=14)
        combobox_14b.insert(0, str(input_text_default))
        input_text = StringVar()

        combobox_14b.pack()

        button_17a = Button(frame5, text='終了', command=lambda: sys.exit())
        button_17a.pack(padx=5, pady=10, expand=True)

        canvasx = min(len(l[0]) * 25, 1800)
        canvasy = min(len(l) * 25, 1000)

        canvas1.title('キャンバス')  # 画面タイトル設定
        canvas1.geometry(str(canvasx) + 'x' + str(canvasy))  # 画面サイズ設定
        ymax = len(l) + 1
        xmax = len(l[0]) + 1
        canvas1.canvas_frame = [[None for j in range(xmax)] for i in range(ymax)]
        canvas1.button_frame = [[None for j in range(xmax)] for i in range(ymax)]
        for y in range(ymax):
            for x in range(xmax):
                if x == 0 and y == 0:
                    pass
                elif x == 0:
                    canvas1.canvas_frame[y][x] = Frame(canvas1, width=25, height=25)
                    canvas1.canvas_frame[y][x].propagate(False)
                    canvas1.canvas_frame[y][x].grid(row=y, column=x)
                    alphaNum = ""
                    numJyu = y // 26
                    numIchi = y % 26
                    if numJyu <= 0 or (numJyu == 1 and numIchi == 0):
                        alphaNum = numToAlpha.numToAlphaOne(numIchi)
                    elif numJyu <= 26:
                        alphaNum = numToAlpha.numToAlphaOne(numJyu) + numToAlpha.numToAlphaOne(numIchi)
                    else:
                        messagebox.showinfo('エラー', '縦スクウェアが上限（675）を超えています')
                        sys.exit()
                    # ★ x,y をデフォルト引数で束縛して遅延束縛を回避
                    canvas1.button_frame[y][x] = Label(
                        canvas1.canvas_frame[y][x],
                        text=alphaNum,
                        font=('System', 14),
                    )
                    canvas1.button_frame[y][x].pack()
                elif y == 0:
                    canvas1.canvas_frame[y][x] = Frame(canvas1, width=25, height=25)
                    canvas1.canvas_frame[y][x].propagate(False)
                    canvas1.canvas_frame[y][x].grid(row=y, column=x)
                    # ★ x,y をデフォルト引数で束縛して遅延束縛を回避
                    canvas1.button_frame[y][x] = Label(
                        canvas1.canvas_frame[y][x],
                        text=str(x),
                        font=('System', 14),
                    )
                    canvas1.button_frame[y][x].pack()
                else:
                    canvas1.canvas_frame[y][x] = Frame(canvas1, width=25, height=25)
                    canvas1.canvas_frame[y][x].propagate(False)
                    canvas1.canvas_frame[y][x].grid(row=y, column=x)
                    # ★ x,y をデフォルト引数で束縛して遅延束縛を回避
                    canvas1.button_frame[y][x] = Button(
                        canvas1.canvas_frame[y][x],
                        text=l[y-1][x-1],
                        font=('System', 14),
                        command=lambda xi=x, yi=y: self.editStart(
                            str(xi+1), str(yi+1), "1", "1", combobox_14b.get()
                        ))
                    canvas1.button_frame[y][x].pack()

        self.canvas = canvas1
        root.mainloop()

    def editStart(self, text_text_xpos, text_text_ypos, text_text_xwidth, text_text_ywidth,
                  text_input_text):

        print(text_text_xpos)
        print(text_text_xpos)
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
            messagebox.showinfo('エラー', '「テキスト横幅」には数値を入力してください。')
            errFlg = True

        text_ywidth = text_text_ywidth
        if text_text_ywidth.isdecimal() or text_text_ywidth == "":
            text_ywidth = int(text_text_ywidth)
        else:
            messagebox.showinfo('エラー', '「テキスト縦幅」には数値を入力してください。')
            errFlg = True

        input_text = text_input_text

        if not errFlg:
            textPos.edit(text_xpos, text_ypos, text_xwidth, text_ywidth,
                         input_text)
            x = int(text_text_xpos) - 1
            y = int(text_text_ypos) - 1
            self.canvas.button_frame[y][x]["text"] = text_input_text


if __name__ == "__main__":
    Program()