import random
import csv

def edit(start_xpos=1, start_ypos=1, start_xwidth=2, start_ywidth=2,
         escape_xpos=1, escape_ypos=1, escape_xwidth=1, escape_ywidth=1):
    outputcsv = ""
    with open('input_map_csv.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        for row in reader:
            print(row)

        xmax = len(l[0])
        ymax = len(l)

        start_xpos_minus = start_xpos - 1
        start_ypos_minus = start_ypos - 1
        escape_xpos_minus = escape_xpos - 1
        escape_ypos_minus = escape_ypos - 1

        for y in range(start_xwidth):
            for x in range(start_ywidth):
                l[start_ypos_minus + y][start_xpos_minus + x] = "初"

        for y in range(escape_xwidth):
            for x in range(escape_ywidth):
                l[escape_ypos_minus + y][escape_xpos_minus + x] = "×"

        for row in l:
            print(row)

        outputcsv = l

    with open('input_map_csv.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(outputcsv)

    return