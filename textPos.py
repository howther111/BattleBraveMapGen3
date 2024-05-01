import random
import csv

def edit(start_xpos=1, start_ypos=1, start_xwidth=2, start_ywidth=2,
         input_text="赤"):
    outputcsv = ""
    with open('input_map_csv.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]

        start_xpos_minus = start_xpos - 1
        start_ypos_minus = start_ypos - 1

        for y in range(start_xwidth):
            for x in range(start_ywidth):
                l[start_ypos_minus + y][start_xpos_minus + x] = input_text

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

    with open('input_map_csv.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(outputcsv)

    return