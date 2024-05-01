import random
import csv

def edit(start_xpos=1, start_ypos=1, start_xwidth=2, start_ywidth=2,
         input_text="赤"):
    outputcsv = ""
    with open('input_map_csv.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        for row in reader:
            print(row)

        #xmax = len(l[0])
        #ymax = len(l)

        start_xpos_minus = start_xpos - 1
        start_ypos_minus = start_ypos - 1

        for y in range(start_xwidth):
            for x in range(start_ywidth):
                l[start_ypos_minus + y][start_xpos_minus + x] = input_text

        for row in l:
            print(row)

        outputcsv = l

    with open('input_map_csv.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(outputcsv)

    return